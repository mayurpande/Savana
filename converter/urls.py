from django.urls import path

from . import views

urlpatterns = [
    path('pdf/', views.pdf, name='pdf'),
    path('txt/', views.txt, name='txt'),
]