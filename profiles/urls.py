from django.urls import path

from .views import profiles_home_view
#from .views import <views_to_import> ...

app_name = 'profiles'

urlpatterns = [
    path('', profiles_home_view, name='profiles-home-view'),  #Example home_view
]