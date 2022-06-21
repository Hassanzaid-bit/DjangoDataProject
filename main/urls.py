from django.urls import include, path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home_screen, name="home_screen"),
    path("/login", views.login_screen, name="login_screen")
]
