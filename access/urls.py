from django.urls import path
from .views import access_login_view, access_logout_view

app_name = "access"   


urlpatterns = [
    path("login/", access_login_view, name="access-login"),
    path("logout/", access_logout_view, name="access-logout")
]