"""qbank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from questions import views

urlpatterns = [
    path('house/', admin.site.urls),

    # Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login/', views.loginuser, name='loginuser'),

    # Questions
    path('', views.home, name='home'),
    path('current/', views.currentquestions, name='currentquestions'),
    path('create/', views.createquestion, name='createquestion'),
    path('questions/<int:question_pk>', views.viewquestion, name='viewquestion'),
    path('questions/<int:question_pk>/complete>', views.completequestion, name='completequestion'),
    path('questions/<int:question_pk>/delete>', views.deletequestion, name='deletequestion'),
]
