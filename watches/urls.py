from django.urls import path
from . import views

# working code
urlpatterns = [
    path('', views.home, name='home'),
    path('add_edit', views.add_edit, name='add_edit'),
    path('<str:list_name>', views.home, name='watch_list')
]
