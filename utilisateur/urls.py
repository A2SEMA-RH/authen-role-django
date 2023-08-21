from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('inscription/', views.register, name='inscription'),
    path('acces/', views.login_view, name='acces'),
    path('adminpage/', views.admin, name='adminpage'),
    path('etudiant/', views.etudiant, name='etudiantPage'),
    path('enseignant/', views.enseignant, name='enseignant'),
]
