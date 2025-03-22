from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm

# Signup View
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Login View
def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
           full_name= form.cleaned_data.get('full_name')
           
           user = authenticate(full_name=full_name )
        if user is not None:
                login(request, user)
                return redirect('landing_page')   
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout View
@login_required
def user_logout(request):
    logout(request)
    return redirect('landing_page')