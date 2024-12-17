from django import forms
from .models import Field, YearlyFieldData
from datetime import datetime

class FieldForm(forms.ModelForm):
    LOCATION_CHOICES = [
        ('', 'Select Location'),
        ('Rowena', 'Rowena'),
        ('Bridgewater', 'Bridgewater')
    ]
    
    location = forms.ChoiceField(
        choices=LOCATION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Field
        fields = ['name', 'location']

class YearlyFieldDataForm(forms.ModelForm):
    CROP_CHOICES = [
        ('', 'Select Crop'),
        ('Corn', 'Corn'),
        ('Soybeans', 'Soybeans'),
        ('Wheat', 'Wheat'),
        ('Oats', 'Oats'),
        ('Alfalfa', 'Alfalfa'),
        ('Grass', 'Grass'),
        ('Other', 'Other'),
    ]

    def __init__(self, *args, field=None, **kwargs):
        super().__init__(*args, **kwargs)
        if field and not self.instance.pk:  # Only for new entries
            # Get most recent year's data
            latest_data = YearlyFieldData.objects.filter(field=field).order_by('-year').first()
            if latest_data:
                self.fields['acres'].initial = latest_data.acres

    custom_crop = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    year = forms.IntegerField(
        initial=datetime.now().year,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    crop = forms.ChoiceField(
        choices=CROP_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = YearlyFieldData
        fields = ['year', 'crop', 'acres', 'seed_cost', 'fertilizer_cost', 
                 'chemical_cost', 'crop_insurance', 'yield_amount']
        widgets = {
            'acres': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter acres'}),
            'seed_cost': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter seed cost'}),
            'fertilizer_cost': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter fertilizer cost'}),
            'chemical_cost': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter chemical cost'}),
            'crop_insurance': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter insurance cost'}),
            'yield_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter yield in bushels'}),
        }