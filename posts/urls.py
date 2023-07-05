from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:id>/delete/', views.delete, name='delete'),

    path('<int:id>/comments/create/', views.comments_create, name='comments_create'),

    path('<int:id>/likes/', views.likes, name='likes'),

]
