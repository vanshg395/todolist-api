from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create/view/', views.TaskAdder.as_view()),
    path('update/view/', views.TaskModifier.as_view()),
]
