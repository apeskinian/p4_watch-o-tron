from django import forms
from .models import Watch, WatchList, WatchMovement

class WatchForm(forms.ModelForm):
    class Meta:
        model = Watch
        fields = (
            'make',
            'collection',
            'model',
            'movement_model',
            'complication_chronograph',
            'complication_date',
            'complication_day',
            'complication_gmt',
            'complication_world_timer',
            'complication_moonphase',
            'complication_power_reserve',
            'complication_tourbillon',
            'image',
            'list_name',
        )