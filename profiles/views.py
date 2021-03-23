from django.shortcuts import render

from django.contrib.auth.decorators import login_required

# Create your views here.ç
@login_required(redirect_field_name='', login_url='/admin')
def profiles_home_view(request):
    return render(request, 'profile-home.html', {}) #This will be the main page for the service