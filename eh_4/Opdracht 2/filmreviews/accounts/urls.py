from django.urls import path
from . import views

urlpatterns = [
    path('registreer/', views.registreer, name='registreer'),
    path('loguit/', views.loguit, name='loguit'),
    path('login/', views.loginaccount, name='login'),
]