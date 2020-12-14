from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('welcome', views.welcome, name='welcome'),
    path('signup', views.signup, name='signup'),
]