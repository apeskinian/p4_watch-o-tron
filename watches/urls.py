from django.urls import path
from django.conf.urls import handler400
from django.shortcuts import render
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('<str:list_name>', views.home, name='watch_list'),
    path(
        'cancel_process/<str:content>/<path:cancel_url>',
        views.cancel_process, name='cancel_process'
    ),
    path('delete/list/<list_id>', views.delete_list, name='delete_list'),
    path(
        'delete/movement/<movement_id>',
        views.delete_movement, name='delete_movement'
    ),
    path('delete/watch/<watch_id>', views.delete_watch, name='delete_watch'),
    path('edit/list/<int:list_id>', views.edit_list, name='edit_list'),
    path(
        'edit/movement/<int:movement_id>',
        views.edit_movement, name='edit_movement'
    ),
    path('leaving_manage/<str:content>',
        views.leaving_manage, name='leaving_manage'
    ),
    path(
        'manage_watch/<str:origin>',
        views.manage_watch, name='manage_watch'
    ),
    path(
        'manage_watch/<str:origin>/<watch_id>',
        views.manage_watch, name='manage_watch'
    ),
    path('purchase/<watch_id>', views.purchase_watch, name='purchase'),
    path('staff_settings/', views.staff_settings, name='staff_settings'),
]


def bad_request(request, exception):
    return render(request, '400.html', status=400)

handler400 = bad_request
