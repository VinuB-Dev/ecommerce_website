from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('pay', views.pay, name='pay'),
    path('Thank', views.Thank, name='Thank'),
    path('track', views.track, name='track'),

]