from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # CREATE
    path("signup/", views.signup, name='signup'),
    # UPDATE
    path("edit/", views.edit, name='edit'),
    # CREATE
    path("login/", views.login, name='login'),
    # DELETE
    path("logout/", views.logout, name='logout'),
    # READ
    path("<str:username>/", views.profile, name='profile'),

    # CREATE
    path('<int:id>/following/', views.following, name='following')
]