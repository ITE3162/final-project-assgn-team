from django.urls import path
from .import views

app_name='blogs'

urlpatterns = [
    path('', views.blog_post, name='blog_home'),
    path('<str:slug>', views.post_detail, name='detail'),
    path('search/search-post', views.search_post, name='search')
]
