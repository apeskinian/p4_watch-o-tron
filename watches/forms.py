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
            'complication_chronograph': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'role': 'switch',
            }),
        }

class MovementForm(forms.ModelForm):    
    class Meta:
        model = WatchMovement
        fields = ['movement_name']

    movement_name = forms.CharField(max_length=200, label=False)


    def clean_name(self):
        movement_name = self.cleaned_data.get('movement_name')
        if WatchMovement.objects.filter(movement_name=movement_name).exists():
            raise forms.ValidationError(f"The movement '{movement_name}' already exists.")
        return movement_name


class ListForm(forms.ModelForm):
    class Meta:
        model = WatchList
        fields = ['list_name']

    list_name = forms.CharField(max_length=200, label=False)

    def clean_name(self):
        list_name = self.cleaned_data.get('list_name')
        if WatchList.objects.filter(list_name=list_name).exists():
            raise forms.ValidationError(f"The list '{list_name}' already exists.")
        return list_name

