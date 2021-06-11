from django.urls import path

from . import views

urlpatterns = [
    path('', views.personel, name='personel'),
    path('active/', views.active, name='active'),
    path('inactive/', views.inactive, name='inactive')

]