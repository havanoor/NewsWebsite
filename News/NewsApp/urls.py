from django.contrib import admin
from django.urls import path
from . import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    
path('',user_views.HomeView.as_view(),name="Home"),
path('topic/<str:topic>',user_views.TopicView.as_view(),name="Topic"),
path('login/',user_views.loginUser,name="logiin"),
path('login2/',auth_views.LoginView.as_view(template_name='login.html')),
path('register/',user_views.register,name="register"),
path('test/',user_views.test,name='test'),


]