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
from registration.views import LoginView,AboutView,ConveyorView,ProfileView,SignupView,HomeView,RealtimeMaintenanceView,SystemDetailsView,UserPageView,CreateSystemView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',LoginView,name='login'),
    path('',HomeView,name='home'),
    # path('indexan',indexview),
    path('about/',AboutView,name='about'),
    # path('contact/',ContactView,name='contact'),
    path('conveyor/',ConveyorView,name='conveyor'),
    path('profile/',ProfileView,name='profile'),
    # path('maintenance/',MaintenanceView,name='maintenance'),
    # path('test/',TestView,name='test'),
    path('signup/',SignupView,name='signup'),
    # path('home/',HomeView,name='home'),
    path('realtime/',RealtimeMaintenanceView,name='realtime'),
    path('systemdetails/',SystemDetailsView,name='systemdetails'),
    path('userpage/',UserPageView,name='userpage'),
    path('createsystem/',CreateSystemView,name='createsystem'),
    # path('verification/',VerificationView,name='verification')
]
