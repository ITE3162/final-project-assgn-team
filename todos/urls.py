from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from . import views

app_name = 'todos'

urlpatterns = [

    path('<str:title>/', views.activity, name='what_we_do'),
]
