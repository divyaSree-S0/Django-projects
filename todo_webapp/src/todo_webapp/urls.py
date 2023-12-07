"""
URL configuration for todo_webapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from todoapp.views import todoappView,addTodoView,deleteTodoView
from registration.views import loginView,signupView,adminloginView,taskView,logoutView,addTaskView,deleteTaskView,userloginView#,homeView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todoapp/',todoappView),
    path('userpage/',taskView),
    path('addtodo/',addTodoView),
    path('deletetodo/<int:i>/',deleteTodoView),
    path('', loginView, name='login'),
    path('adminlogin/', adminloginView, name='adminlogin'),
    path('signup/',signupView,name='signup'),
    # path('home/',homeView),
    path('logout/', logoutView, name='logout'),
    path('add_task/', addTaskView, name='add_task'),
    path('deletetask/<int:i>/',deleteTaskView),
    path('user_page/',userloginView,name='user_page')
]
urlpatterns += staticfiles_urlpatterns()