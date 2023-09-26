from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Chat
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
def ChatView (request, frienduuid) : 
    context = {}

    return render(request,'chat_app/chat.html',context)


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