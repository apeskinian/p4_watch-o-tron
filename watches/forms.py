from django import forms
from .models import Watch, WatchList, WatchMovement

class WatchForm(forms.ModelForm):
    class Meta:
        model = Watch
        fields = [
            'make',
            'collection',
            'model',
            'movement_type',
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
        ]

    movement_type = forms.ModelChoiceField(
        queryset=WatchMovement.objects.all(),
        empty_label='Select a movement',
        required=True,
        widget=forms.Select(attrs={'class': 'browser-default'})
    )

    list_name = forms.ModelChoiceField(
        queryset=WatchList.objects.all(),
        empty_label='Select a list',
        required=True,
        widget=forms.Select(attrs={'class': 'browser-default'})
    )

    complication_chronograph = forms.BooleanField(
        label='Chronograph',
        required=False
    )
    
    complication_date = forms.BooleanField(
        label='Date',
        required=False
    )

    complication_day = forms.BooleanField(
        label='Day',
        required=False
    )

    complication_gmt = forms.BooleanField(
        label='GMT',
        required=False
    )

    complication_world_timer = forms.BooleanField(
        label='World Timer',
        required=False
    )
    
    complication_moonphase = forms.BooleanField(
        label='Moonphase',
        required=False
    )

    complication_power_reserve = forms.BooleanField(
        label='Power Reserve',
        required=False
    )

    complication_tourbillon = forms.BooleanField(
        label='Tourbillon',
        required=False
    )