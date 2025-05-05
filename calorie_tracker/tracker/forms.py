from django import forms
from .models import FoodEntry

class FoodEntryForm(forms.ModelForm):
    date_consumed = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
    )
    
    class Meta:
        model = FoodEntry
        fields = ['food_name', 'calories', 'date_consumed']
        widgets = {
            'food_name': forms.TextInput(attrs={'class': 'form-control'}),
            'calories': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class DateFilterForm(forms.Form):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False
    )
