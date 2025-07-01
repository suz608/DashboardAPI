import os
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

frontend_url = os.getenv("FRONTEND_URL", "http://localhost:4200")  

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user
            login(request, user)  # Log the user in immediately after registration
            return redirect(frontend_url) 
    else:
        form = UserCreationForm()  # Initialize the form for GET request

    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()  # Get the user from the form
            login(request, user)  # Log the user in
            return redirect(frontend_url) 
    else:
        form = AuthenticationForm()  # Initialize the form for GET request

    return render(request, "login.html", {"form": form})
