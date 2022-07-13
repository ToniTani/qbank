from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import CreateQuestion
from .models import Question
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'questions/home.html')

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

@login_required
def logoutuser(request):
    if request.method == 'POST':
            logout(request)
            return redirect('home')

@login_required
def currentquestions(request):
    questions = Question.objects.filter(user=request.user, datecompleted__isnull=True)
    # questions = Question.objects.filter(user=request.user)
    # questions = Question.objects.all()
    return render(request, 'questions/currentquestions.html', {'questions':questions})

@login_required
def viewquestion(request, question_pk):
    question = get_object_or_404(Question, pk=question_id, user=request.user)
    if request.method == 'GET':
        form = CreateQuestion(instance=question)
        return render(request, 'questions/viewquestion.html', {'question':question, 'form':form})
    else:
        try:
            form = CreateQuestion(request.POST, instance=question)
            form.save()
            return redirect('currentquestions')
        except ValueError:
            return render(request, 'questions/viewquestion.html', {'question':question, 'form':form, 'error':'Bad input!'})

@login_required
def createquestion(request):
    if request.method == 'GET':
        return render(request, 'questions/createquestion.html', {'form':CreateQuestion()})
    else:
        try:
            form = CreateQuestion(request.POST)
            newquestion= form.save(commit=False)
            newquestion.user = request.user
            newquestion.save()
            return redirect('currentquestions')
        except ValueError:
            return render(request, 'questions/createquestion.html', {'form':CreateQuestion(), 'error': 'Bad data inserted. Please try again!'})

@login_required
def completequestion(request, question_pk):
    question = get_object_or_404(Question, pk=question_id, user=request.user)
    if request.method == 'POST':
        question.datecompleted = timezone.now()
        question.save()
        return redirect('currentquestions')

@login_required
def deletequestion(request, question_pk):
    question = get_object_or_404(Question, pk=question_id, user=request.user)
    if request.method == 'POST':
        question.delete()
        return redirect('currentquestions')

@login_required
def listedquestions(request):
    questions = Question.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'questions/listedquestions.html', {'questions':questions})
