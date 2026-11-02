"""Corporate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from CorporateApp import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('login',views.login_user,name='login'),
    path('adminlogin',views.admin,name = 'admin'),
    path('register',views.register,name = 'register'),
    path('logout',views.logout_user,name='logout'),
    path('add_training', views.add_training, name='add_training'), 
    #path('enroll', views.enroll, name='enroll'),
    path('enroll_list', views.enroll_list, name='enroll_list'),
    path('training_list',views.training_list,name='training_list'),
    path('delete_training/<int:training_id>/', views.delete_training, name='delete_training'),
    path('available_courses', views.available_courses, name='available_courses'),
    path('enroll_course/<int:pk>',views.enroll_user, name = 'enroll_user'),



]

