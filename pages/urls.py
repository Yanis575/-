
from django.contrib import admin
from django.urls import path
from .views import info

app_name = 'pages'
urlpatterns = [
    path('', info, name='info')
]
