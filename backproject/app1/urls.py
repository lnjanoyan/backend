from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path("", views.home, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('characters/', views.character_list, name='character_list')
]
