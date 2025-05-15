
from django.contrib import admin
from django.urls import path
from .views import index, seek, question, detail

app_name = 'questions'
urlpatterns = [
    path('', index, name='index'),
    path('seek/', seek, name='seek'),
    path('create/', question, name='create'),
    path('detail/<int:pk>/', detail, name='detail')
]
