from django.shortcuts import render, redirect

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def access_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profiles:profiles-home-view')
    form = AuthenticationForm()
    return render(request, 'login.html', {'login_form': form})


def access_logout_view(request):
    logout(request)
    return redirect('profiles:profiles-home-view')
