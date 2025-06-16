from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process/<str:building>/', views.process, name='process'),
    path('reset', views.reset),
    path('start', views.start_game, name='start_game'),
]