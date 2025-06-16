from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process', views.random_number),
    path('process_winner', views.leader),
    path('leaderboard', views.show_leaderboard),
    path('reset', views.reset),
]