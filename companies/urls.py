from django.urls import path
from . import views

app_name = 'companies'

urlpatterns = [
    path('', views.home, name='home'),
    path('add_review/', views.add_review, name='add_review'),
    path('ajax/', views.search, name='search'),
    path('<int:id>/', views.company, name='company'),

]
