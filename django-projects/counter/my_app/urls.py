from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('increment', views.increment),
    path('destroy_session', views.destroy),
]