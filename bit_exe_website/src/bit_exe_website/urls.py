"""bit_exe_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from registration.views import LoginView,SignupView,HomepageView,LoginSliderView,RegisterView,IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',LoginView,name='login'),
    path('loginslider/',LoginSliderView,name='loginslider'),
    path('signup/',SignupView,name='signup'),
    path('',HomepageView,name='homepage'),
    path('register/',RegisterView,name='register'),
    path('index/',IndexView,name='index'),
]
