from django import forms
from app.models import *


class WeatherForm(forms.ModelForm):
    class Meta:
        model=Weather
        fields=['city']

        widgets={
            "city":forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the city name',
            })
        }