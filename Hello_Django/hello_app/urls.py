from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='hello_app-home'),
    path('about/', views.about, name='hello_app-about')
]
