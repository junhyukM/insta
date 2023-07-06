from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    
    # 주소창엔 언더바를 사용하지 않아서 '-'로 사용
    # READ 부분에서 username으로 bookmark-list 를 인식할 수 있는 문제가 있어(str 이라서) 순서를 위로 올림
    path('bookmark-list/', views.bookmark_list, name='bookmark_list'),

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
    path('<int:id>/following/', views.following, name='following'),

]