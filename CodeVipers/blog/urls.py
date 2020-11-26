from django.contrib import admin
from django.urls import path,include
from blog.views import index,create

urlpatterns = [
    path('',index,name='index'),
    path('create',create,name='create' ),
    
]