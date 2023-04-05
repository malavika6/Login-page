from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def home(request):
    return render(request,"index.html")
def signup(request):
    if 'username'in request.session:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 =request.POST['pass2']
        email = request.POST['email']

     
        if User.objects.filter(username=username).exists():
   
            return render(request, 'signup.html', {'error': 'Username already exists'})


        user = User.objects.create_user(username,email,pass1)

        user.save()
        return redirect('signin')
    else:
        return render(request, 'signup.html')
def signin(request):
    if 'username'in request.session:
        return redirect('home')
    if request.method=="POST":
        username =request.POST['username']
        pass1 =request.POST['pass1']

        user = authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            request.session['username']=username

            return render(request,'index.html')
        else:
            messages.error (request,"Bad Credentials!") 
            return redirect('home')  
         

    return render(request,"signin.html")
def signout(request):
    
    
    if 'username' in request.session:
        request.session.flush()
        logout(request)
    
        return redirect('home') 
    return redirect(request, 'signup.html')
     