from django import forms
from .models import Itinerary, DayPlan
from destinations.models import Destination


class ItineraryForm(forms.ModelForm):
    """Form for creating/editing itineraries"""
    
    class Meta:
        model = Itinerary
        fields = ['destination', 'title', 'start_date', 'days']
        widgets = {
            'destination': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Summer Vacation 2026'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'days': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '30'}),
        }


class DayPlanForm(forms.ModelForm):
    """Form for creating/editing day plans"""
    
    class Meta:
        model = DayPlan
        fields = ['day_number', 'plan']
        widgets = {
            'day_number': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'plan': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 5,
                'placeholder': 'Describe your activities for this day...'
            }),
        }
