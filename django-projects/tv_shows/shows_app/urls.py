from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows/new', views.add),
    path('shows/<int:number>', views.show),
    path('create', views.create),
    path('shows/', views.show_all),
    path('shows/<int:number>/edit', views.edit),
    path('shows/<int:number>/update', views.update),
    path('shows/<int:number>/delete', views.destroy),
]