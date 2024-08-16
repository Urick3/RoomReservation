from django import forms
from .models import Room


class RoomsForm(forms.ModelForm):
    class Meta:

        model = Room
        fields = ['name']
        labels = {
            "name": "Nome",
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Nome da Sala"
                }
            )
        }
