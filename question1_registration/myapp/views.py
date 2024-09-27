# registration/views.py
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def registration_success(request):
    return render(request, 'success.html')
