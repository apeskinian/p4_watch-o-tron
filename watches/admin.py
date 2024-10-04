from django.contrib import admin
from .models import WatchList, WatchMovement, Watch

@admin.register(WatchList)
class WatchListAdmin(admin.ModelAdmin):
    list_display = ('list_name',)

@admin.register(WatchMovement)
class WatchMovementAdmin(admin.ModelAdmin):
    list_display = ('movement_name',)

@admin.register(Watch)
class WatchAdmin(admin.ModelAdmin):
    list_display = ('make', 'collection', 'model', 'owner')
    list_filter = ('owner', 'list_name')