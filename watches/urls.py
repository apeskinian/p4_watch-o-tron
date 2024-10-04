from django.urls import path
from . import views

urlpatterns = [
    path('', views.collection, name='collection'),
    path('collection/', views.collection, name='collection'),
    path('wishlist/', views.wishlist, name='wishlist'),
]