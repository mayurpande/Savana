from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pdf/', views.pdf, name='pdf'),
    path('converted_pdf/', views.converted_pdf, name='converted_pdf')
]