from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('post/(?P<pk>[0-9]+)/', views.detail, name='detail'),
    path('post/(?P<pk>[0-9]+)/leave_comment', views.leave_comment, name='leave_comment'),
    path('post/new/', views.new, name='new'),
    path(r'^post/(?P<pk>[0-9]+)/edit/$', views.edit, name='edit'),
    path(r'^post/(?P<pk>[0-9]+)/delete/$', views.delete, name='delete'),
    path('posts_list', views.posts_list, name='posts_list'),
]

