
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.meeting_list, name='meeting-list'),
    path('new/', views.meeting_create, name='meeting_create'),
    path('<int:pk>/edit/', views.meeting_update, name='meeting_update'),
    path('<int:pk>/delete/', views.meeting_delete, name='meeting_delete'),
]