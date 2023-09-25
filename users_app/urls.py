from django.urls import path
from .views import LoginView, RegisterView, EditView
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('register/',RegisterView,name='register'),
    path('login/',LoginView,name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('edit/',EditView,name='edit'),
]