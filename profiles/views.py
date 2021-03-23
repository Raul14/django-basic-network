from django.shortcuts import render

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def profiles_home_view(request):
    return render(request, 'profile-home.html', {}) #This will be the main page for the service