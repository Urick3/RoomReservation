from reservations.models import *
from django import forms

class HourForm(forms.ModelForm):
    class Meta:

        model = Hour
        fields = 'range_hour'
        labels = {
            'range_hour': 'horario',
        }
        widgets = {
            'range_hour': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Horario",
                }
            ),
        }