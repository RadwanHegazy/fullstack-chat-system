from chat_app.models import Message, Chat
from django.shortcuts import get_object_or_404, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from users_app.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@login_required
def SendImage (request, chatuuid) : 

    chat = get_object_or_404(Chat, uuid=chatuuid)
    sender = request.user
    image = request.FILES['image']
    

    group_name = f'room_{chatuuid}'
    
    msg = Message.objects.create(
        sender = sender,
        chat = chat,
        image = image
    )

    msg.save()

    data = {
        'picture' : sender.picture.url,
        'id' : msg.id,
        'image' : msg.image.url,
        'date' : f'{msg.date}',
        'sender' : sender.full_name,

    }

    event = {
        'type':'send_message',
        'data' : data
    
    }

    channel_layer = get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        group_name,event
    )




    return HttpResponse('Done')


login_required
def SendAudio (request, chatuuid) : 

    chat = get_object_or_404(Chat, uuid=chatuuid)
    sender = request.user
    audio = request.FILES['audio']
    
    audio.name = 'blob.ogg'

    group_name = f'room_{chatuuid}'
    
    msg = Message.objects.create(
        sender = sender,
        chat = chat,
        audio = audio
    )

    msg.save()

    data = {
        'picture' : sender.picture.url,
        'id' : msg.id,
        'audio' : msg.audio.url,
        'date' : f'{msg.date}',
        'sender' : sender.full_name,

    }

    event = {
        'type':'send_message',
        'data' : data
    
    }

    channel_layer = get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        group_name,event
    )




    return HttpResponse('Done')
