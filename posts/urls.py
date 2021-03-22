from django.urls import path

from .views import home_view
#from .views import <views_to_import> ...

app_name = 'posts'

urlpatterns = [
    path('', home_view, name='posts-home-view'),  #Example home_view
]