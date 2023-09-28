from django.urls import path
from . import views

urlpatterns = [
    path('send/image/<str:chatuuid>/',views.SendImage,name='send_img'),
    path('send/audio/<str:chatuuid>/',views.SendAudio,name='send_audio'),

]