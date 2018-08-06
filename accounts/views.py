from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/companies/')
                # return render(request, 'companies/home.html')
    form = LoginForm()
    context = {'form': form, }
    return render(request, 'accounts/login.html', context=context)


def register_user(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/companies/')
    context = {'form': form}
    return render(request, 'accounts/register.html', context=context)



def logout_user(request):
    if request.method == "GET":
        logout(request)
        return redirect('/')
