from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('new', views.new, name="new"),
    path('<int:post_id>/', views.detail, name="detail"),
    path('create/', views.create, name="create"),
    path('modify/<int:post_id>', views.modify, name="modify"),
    path('update/<int:post_id>', views.update, name="update"),
    path('delete/<int:post_id>', views.delete, name="delete"),
    path('newpost/', views.newpost, name="newpost"),
]

