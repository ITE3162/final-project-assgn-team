from django.urls import path,re_path
from .import views

app_name='blogs'

urlpatterns = [
    path('', views.blog_post, name='blog_home'),

    path('create/', views.post_create, name="create"),

    path('<str:slug>', views.post_detail, name='detail'),

    # path('tag/<slug:tag_slug>/', views.blog_post, name='tagged'),
    path('tag/<slug:tag_slug>/', views.blog_post, name='tagged'),
    # re_path(r'^(?P<slug>[\w-]+)/$', views.post_detail, name='detail'),
    path('search/search-post', views.search_post, name='search')
]
