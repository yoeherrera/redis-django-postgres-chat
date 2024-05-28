from django.contrib.auth import authenticate, login as django_login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm  # Import your custom form from forms.py
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('chat:login_view')  # Ensure correct namespace
    else:
        form = CustomUserCreationForm()
    return render(request, 'chat/register.html', {'form': form})

def index(request):
    username = request.session.get('username')
    if not username:
        return redirect('chat:login_view')
    return render(request, 'chat/index.html', {'username': username})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            django_login(request, user)
            return redirect('chat:room')  # Ensure correct namespace
        else:
            return render(request, 'chat/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'chat/login.html')

@login_required
def room(request):
    username = request.user.username
    welcome_message = f"Welcome to the chat, {username}!"
    return render(request, 'chat/room.html', {
        'username': username,
        'welcome_message': welcome_message,
    })