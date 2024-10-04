from django.urls import path
from . import views

# working code
urlpatterns = [
    path('', views.home, name='home'),
]
