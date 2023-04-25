from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from templates.forms import RegisterUserForm


# Create your views here.
def login_view(request):
    template = 'login.html'
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm(request)
    context = {"form": form}
    return render(request, template, context)

"""def login_view(request):
    template = 'login.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username = username, password = password)
        if user is None:
            context = {'error':'Invalid username or password.'}
            return render(request, template, context)
        login(request, user)
        return redirect('/admin')
    return render(request, template, {})"""

def logout_view(request):
    context = locals()
    template = 'logout.html',
    if request.method == 'POST':
        logout(request)
        return redirect('/')
    return render(request, template, context) #string of HTML code

"""def register_view(request):
    template = 'register.html'
    form = RegisterUserForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        messages.success(request, ("Congratulations! Your registration has been successful."))
        return redirect('login/')        

    context = {'form': form}
    return render(request, template, context)"""

def register_view(request):
    template = 'register.html'
    if request.method == 'POST':
        form = RegisterUserForm (request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, ("Congratulations! Your registration has been successful."))
            return redirect('home')        
    else:
        form = RegisterUserForm()
    context = {'form': form}
    return render(request, template, context)

def test_view(request):
    template = 'test.html'
    if request.method == 'POST':
        form = RegisterUserForm (request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, ("Congratulations! Your registration has been successful."))
            return redirect('login/')        
    else:
        form = RegisterUserForm()
    context = {'form': form}
    return render(request, template, context) 