from django.contrib import admin
from django.urls import path
from . import views as user_views

urlpatterns = [
    
path('',user_views.HomeView.as_view(),name="Home"),
path('topic/<str:topic>',user_views.TopicView.as_view(),name="Topic"),


]