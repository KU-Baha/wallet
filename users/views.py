from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')

        messages.error(request, "Invalid username or password.")

    form = AuthenticationForm()
    return render(request=request, template_name="users/login.html", context={"form": form})


def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('index')
