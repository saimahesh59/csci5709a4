from django.urls import path
from . import views

app_name = 'explore'

urlpatterns = [
    path('', views.home, name='home'),

]
