from django.urls import path
from . import views

# working code
urlpatterns = [
    path('', views.collection, name='home'),
    path('collection/', views.collection, name='collection'),
    path('wishlist/', views.wishlist, name='wishlist'),
]
