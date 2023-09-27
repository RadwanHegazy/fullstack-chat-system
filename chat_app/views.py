from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Chat, Message
from users_app.models import User

@login_required
def HomeView (request) : 
    context = {}

    chats = Chat.objects.filter(users=request.user)

    if 's' in request.GET :
        keyword = request.GET['s']
        if keyword :
            chats = chats.filter(users__full_name__icontains=keyword)


    context['chats'] = chats
    return render(request,'chat_app/home.html',context)



@login_required
def ChatView (request, chatuuid) : 

    context = {}
    chat = get_object_or_404(Chat,uuid=chatuuid)

    context['friend'] = chat.get_friend(user=request.user)
    context['messages'] = Message.objects.filter(chat=chat)

    return render(request,'chat_app/chat.html',context)




@login_required
def CreateChat (request, frienduuid) : 
    
    friend = get_object_or_404(User,uuid=frienduuid)
    user = request.user

    chat = Chat.objects.create()
    chat.users.add(friend)
    chat.users.add(user)

    chat.save()

    return redirect('chat',chat.uuid)


@login_required
def SeachFriends (request) : 
    context = {}

    user = request.user
    
    unwanted = [i.get_friend(user).id for i in Chat.objects.all()]
    unwanted.append(user.id)

    
    users = User.objects.exclude(id__in=unwanted)
    
    if 's' in request.GET :
        keyword = request.GET['s']
        if keyword :
            users = users.filter(full_name__icontains=keyword)

    
    context['users'] = users

    return render(request,'chat_app/search_users.html',context)