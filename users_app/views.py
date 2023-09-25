from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.views import auth_login
from django.contrib.auth.decorators import login_required




def LoginView (request): 

    context = {}
    if request.method == "POST" :
        email = request.POST['email']
        password = request.POST['password']

        check_data = User.login(email=email,password=password)

        if check_data['errors'] :
            context['error'] = check_data['errors']
        else :
            user = check_data['user']
            auth_login(request,user=user)

            return redirect('home')


    return render(request,'users_app/login.html', context)


def RegisterView (request) :
    
    if request.method == "POST" : 
        full_name = request.POST['full_name']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(
            email = email,
            password = password ,
            full_name = full_name
        )

        if 'img' in request.FILES :
            user.picture = request.FILES['img']

        user.save()

        auth_login(request,user=user)

        return redirect('home')

    
    return render(request,'users_app/register.html')

@login_required
def EditView (request) :


    if request.method == "POST" : 
        user = request.user
        
        full_name = request.POST['full_name']
        email = request.POST['email']

        user.full_name = full_name
        user.email = email

        if 'img' in request.FILES :
            user.picture = request.FILES['img']

        user.save()

        return redirect('home')

    
    return render(request,'users_app/edit.html')

