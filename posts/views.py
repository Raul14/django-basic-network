from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'post-home.html', {}) #This will be the main page for the service