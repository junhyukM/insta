from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # READ
    path('', views.index, name='index'),
    # CREATE
    path('create/', views.create, name='create'),
    # DELETE
    path('<int:id>/delete/', views.delete, name='delete'),

    # CREATE
    path('<int:id>/comments/create/', views.comments_create, name='comments_create'),
    
    path('<int:id>/likes/', views.likes, name='likes'),

]
