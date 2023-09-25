from django.urls import path
from . import views


urlpatterns = [
    path('',views.HomeView,name='home'),
    path('chat/<str:frienduuid>/',views.ChatView,name='chat'),
    path('search-users/',views.SeachFriends,name='search_users'),
]