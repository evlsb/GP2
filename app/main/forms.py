from .models import *
from django.forms import ModelForm, TextInput, Select, ChoiceField


class SensorForm(ModelForm):

    class Meta:
        model = Sensor
        fields = ['position', 'description', 'cat', 'units']

        widgets = {
            "position": TextInput(attrs={
                'class': 'form-control mt-2',
                'placeholder': 'Позиционный номер',
                'aria-describedby': 'position'
            }),
            "description": TextInput(attrs={
                'class': 'form-control mt-2',
                'placeholder': 'Описание',
                'aria-describedby': 'description'
            }),
            "cat": Select(attrs={
                'class': 'form-select form-control mt-2',
                'placeholder': 'Описание',
                'aria-describedby': 'description'
            }),
            "units": Select(attrs={
                'class': 'form-select form-control mt-2',
                'placeholder': 'Описание',
                'aria-describedby': 'description'
            })
        }


class EngUnitsForm(ModelForm):

    class Meta:
        model = EngUnits
        fields = ['name']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control mt-2',
                'placeholder': 'Единицы измерения',
                'aria-describedby': 'position'
            })
        }


class CategoryForm(ModelForm):

    class Meta:
        model = Category
        fields = ['name']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control mt-2',
                'placeholder': 'Категория',
                'aria-describedby': 'position'
            })
        }