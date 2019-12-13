from django.urls import path, include
from django.contrib.auth.decorators import login_required
from . import views as viewsu

app_name= "users"
urlpatterns = [

path('registro', viewsu.RegisterUsers.as_view(),name='users_register'),

]
