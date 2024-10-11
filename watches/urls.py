from django.urls import path
from . import views

# working code
urlpatterns = [
    path('', views.home, name='home'),
    path('add_watch', views.add_watch, name='add_watch'),
    path('delete/watch/<watch_id>', views.delete_watch, name='delete_watch'),
    path('delete/movement/<movement_id>', views.delete_movement, name='delete_movement'),
    path('delete/list/<list_id>', views.delete_list, name='delete_list'),
    path('edit/<watch_id>', views.edit_watch, name='edit_watch'),
    path('purchase/<watch_id>', views.purchase_watch, name='purchase'),
    path('staff_settings', views.staff_settings, name='staff_settings'),
    path('edit/movement/<int:movement_id>', views.edit_movement, name='edit_movement'),
    path('edit/list/<int:list_id>', views.edit_list, name='edit_list'),
    path('<str:list_name>', views.home, name='watch_list'),
]
