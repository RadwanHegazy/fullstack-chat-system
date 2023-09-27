from django.urls import path
from . import views


urlpatterns = [
    path('',views.HomeView,name='home'),
    path('chat/<str:chatuuid>/',views.ChatView,name='chat'),
    path('create-chat/<str:frienduuid>/',views.CreateChat,name='create_chat'),
    path('search-users/',views.SeachFriends,name='search_users'),
]