from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('add_watch/<str:origin>', views.add_watch, name='add_watch'),
    path(
        'cancel_process/<str:content>/<path:cancel_url>',
        views.cancel_process, name='cancel_process'
    ),
    path('delete/watch/<watch_id>', views.delete_watch, name='delete_watch'),
    path(
        'delete/movement/<movement_id>',
        views.delete_movement, name='delete_movement'
    ),
    path('delete/list/<list_id>', views.delete_list, name='delete_list'),
    path('edit/list/<int:list_id>', views.edit_list, name='edit_list'),
    path(
        'edit/movement/<int:movement_id>',
        views.edit_movement, name='edit_movement'
    ),
    path(
        'edit/watch/<watch_id>/<str:origin>',
        views.edit_watch, name='edit_watch'
    ),
    path('purchase/<watch_id>', views.purchase_watch, name='purchase'),
    path('staff_settings/', views.staff_settings, name='staff_settings'),
    path('<str:list_name>', views.home, name='watch_list'),
]
