from django import forms
from django.contrib.auth.forms import UserCreationForm
from rooms.models import *


class ItensRooms(forms.ModelForm):
    class Meta:

        model = Room
        fields = "__all__"
        labels = {
            "name": "nome",
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Nome da Sala",
                }
            ),
        }
