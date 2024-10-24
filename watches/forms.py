from django import forms
from django.contrib.auth.forms import UserCreationForm
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
        widgets = {
            'make': forms.TextInput(attrs={
                'style': 'width: 100%;',
                'class': 'form-control',
            }),
            'collection': forms.TextInput(attrs={
                'style': 'width: 100%;',
                'class': 'form-control',
            }),
            'model': forms.TextInput(attrs={
                'style': 'width: 100%;',
                'class': 'form-control',
            }),
            'movement_type': forms.Select(attrs={
                'style': 'width: 100%;',
                'class': 'form-control',
            }),
            'movement_model': forms.TextInput(attrs={
                'style': 'width: 100%;',
                'class': 'form-control',
            }),
            'complication_chronograph': forms.CheckboxInput(attrs={
                'style': 'height: 25px; width: 40px;',
                'class': 'form-check-input',
                'role': 'switch',
            }),
            'complication_date': forms.CheckboxInput(attrs={
                'style': 'height: 25px; width: 40px;',
                'class': 'form-check-input',
                'role': 'switch',
            }),
            'complication_day': forms.CheckboxInput(attrs={
                'style': 'height: 25px; width: 40px;',
                'class': 'form-check-input',
                'role': 'switch',
            }),
            'complication_gmt': forms.CheckboxInput(attrs={
                'style': 'height: 25px; width: 40px;',
                'class': 'form-check-input',
                'role': 'switch',
            }),
            'complication_world_timer': forms.CheckboxInput(attrs={
                'style': 'height: 25px; width: 40px;',
                'class': 'form-check-input',
                'role': 'switch',
            }),
            'complication_moonphase': forms.CheckboxInput(attrs={
                'style': 'height: 25px; width: 40px;',
                'class': 'form-check-input',
                'role': 'switch',
            }),
            'complication_power_reserve': forms.CheckboxInput(attrs={
                'style': 'height: 25px; width: 40px;',
                'class': 'form-check-input',
                'role': 'switch',
            }),
            'complication_tourbillon': forms.CheckboxInput(attrs={
                'style': 'height: 25px; width: 40px;',
                'class': 'form-check-input',
                'role': 'switch',
            }),
            'image': forms.FileInput(attrs={
                'style': 'width: 100%;',
                'class': 'form-control',
            }),
            'list_name': forms.Select(attrs={
                'style': 'width: 100%;',
                'class': 'form-control',
            }),
        }
        labels = {
            'complication_chronograph': 'Chronograph',
            'complication_date': 'Date',
            'complication_day': 'Day',
            'complication_gmt': 'GMT',
            'complication_world_timer': 'World Timer',
            'complication_moonphase': 'Moonphase',
            'complication_power_reserve': 'Power Reserve',
            'complication_tourbillon': 'Tourbillon',
        }


class MovementForm(forms.ModelForm):
    class Meta:
        model = WatchMovement
        fields = ['movement_name']

    movement_name = forms.CharField(max_length=100, label=False)

    def clean_name(self):
        movement_name = self.cleaned_data.get('movement_name')
        if WatchMovement.objects.filter(movement_name=movement_name).exists():
            raise forms.ValidationError()
        return movement_name


class ListForm(forms.ModelForm):
    class Meta:
        model = WatchList
        fields = ['friendly_name']

    friendly_name = forms.CharField(max_length=100, label=False)

    def clean_name(self):
        friendly_name = self.cleaned_data.get('friendly_name')
        if WatchList.objects.filter(friendly_name=friendly_name).exists():
            raise forms.ValidationError()
        return friendly_name
