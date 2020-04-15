from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.normal, name='normal'),
    path('', views.newMains, name='mains'),
]
