from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required




@login_required
def HomeView (request) : 
    context = {}

    return render(request,'chat_app/home.html',context)

@login_required
def ChatView (request, frienduuid) : 
    context = {}

    return render(request,'chat_app/chat.html',context)

@login_required
def SeachFriends (request) : 
    context = {}

    return render(request,'chat_app/search_users.html',context)