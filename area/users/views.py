from django.contrib import auth
from django.http import HttpResponseRedirect

from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrtionForm, UserProfileForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:main'))    
    else:
        form = UserLoginForm()      
    form = UserLoginForm()
    context = {
        'main':'Главная страница - Авторизация',
        'form': form,
        }
    return render(request, 'users/login.html', context)



def registration(request):
    if request.method == 'POST':
        form = UserRegistrtionForm(data=request.POST)
        if form.is_valid():
            form.save()
            user=form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main:main'))    
    else:
        form = UserRegistrtionForm()

    context= {
        'main':'Главная страница - Регистрация',
        'form': form,
        }
    return render(request, 'users/registration.html', context)



def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            user=form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('users:profile'))    
    else:
        form = UserProfileForm(instance=request.user)

    context={
        'main':'Главная страница - Профиль',
        'form':form
        }
    return render(request, 'users/profile.html', context)




def logout(request):
    auth.logout(request)
    return redirect(reverse('main:main'))










