from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate

def home(request):
    return render(request, 'questions/home.html'

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'questions/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currentquestions')
            except IntegrityError:
                return render(request, 'questions/signupuser.html', {'form':UserCreationForm(), 'error':'Username has already been taken, Please choose a new username' })

        else:
            return render(request, 'questions/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match' })
            # User doesnt match

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'questions/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'questions/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match!'})
        else:
            login(request, user)
            return redirect('currentquestions')
            
def logoutuser(request):
    if request.method == 'POST':
            logout(request)
            return redirect('home')

def currentquestions(request):
    return render(request, 'questions/currentquestions.html')
