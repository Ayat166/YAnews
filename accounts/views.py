from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.models import User
import re
from django.contrib import auth

# Create your views here.
def login(request):
    if request.method == 'POST' and 'btnlogin' in request.POST:
        username=request.POST['user']
        password=request.POST['pass']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
        else:
            messages.error(request,'Username and password invalid')
        return redirect('login')

    return render(request,'accounts/login.html')

def signup(request):
    if request.method == 'POST' and 'btnsignup' in request.POST:
        username=None
        email = None
        password=None
        if 'username' in request.POST:username=request.POST['username']
        else:messages.error(request,'Error in first name')
        if 'email' in request.POST:email=request.POST['email']
        else:messages.error(request,'Error in email')
        if 'pass' in request.POST:password=request.POST['pass']
        else:messages.error(request,'Error in password')
        if username and email and password:
            if User.objects.filter(username=username).exists():
                messages.error(request,'This username is taken')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'this email is taken')
                else:
                    patt ="^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$"
                    if re.match(patt,email):
                        user = User.objects.create_user(email=email,
                                                            username=username,
                                                            password=password)
                        user.save()
                        email=''
                        username=''
                        password=''
                        messages.success(request,'The Account created successfully')
                    else:
                            messages.error(request,'Invaild email')
        else:
            messages.error(request,'Check empty fields') 
        return render(request,'accounts/signup.html',{
            'email':email,
            'pass':password,
            'user':username,
        })
    else :
        return render(request,'accounts/signup.html')
    
    
    
def logout(requset):
    if requset.user.is_authenticated:
        auth.logout(requset)
    return redirect('index')



def profile(request):
    if request.method == 'POST' and 'btnsave' in request.POST:
        if request.user is not None and request.user.id != None:
            if request.POST['pass']:
                if not request.POST['pass'].startswith('pbkdf2_sha256$'):
                    request.user.set_password(request.POST['pass']) 
                request.user.save()
                auth.login(request, request.user)
                messages.success(request,'your data has been saved')
            else:
                messages.error(request,'check your values')
        return redirect('profile')
    else:
        if request.user is not None :
            context=None
            if not request.user.is_anonymous:
                context={
                   'pass':request.user.password
                }
            return render(request,'accounts/profile.html',context)
        else:
            return redirect('profile')
    