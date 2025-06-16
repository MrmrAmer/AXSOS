from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create', views.create),
    path('books/<int:number>', views.show),
    path('books/<int:number>/add_author', views.add_author, name='add_author'),
    path('authors', views.authors),
    path('create_author', views.create_author),
    path('authors/<int:number>', views.show_author),
    path('authors/<int:number>/add_book', views.add_book, name='add_book'),
]