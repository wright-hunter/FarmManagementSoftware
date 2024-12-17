from django import forms
from .models import Equipment, EquipmentExpense
from datetime import datetime

class EquipmentForm(forms.ModelForm):
    EQUIPMENT_TYPES = [
        ('', 'Select Type'),
        ('Tractor', 'Tractor'),
        ('Combine', 'Combine'),
        ('Planter', 'Planter'),
        ('Sprayer', 'Sprayer'),
        ('Tillage', 'Tillage'),
        ('Trailer', 'Trailer'),
        ('Other', 'Other')
    ]

    custom_type = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    year = forms.IntegerField(
        initial=datetime.now().year,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    
    equipment_type = forms.ChoiceField(
        choices=EQUIPMENT_TYPES,
        required=True,  # Changed to True
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Equipment
        fields = ['make', 'model', 'year']  # Remove 'type' from here
        widgets = {
            'make': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter make'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter model'}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        equipment_type = cleaned_data.get('equipment_type')
        custom_type = cleaned_data.get('custom_type')
        
        if equipment_type == 'Other' and not custom_type:
            raise forms.ValidationError("Please specify a custom type")
        
        # Add the type field to cleaned_data
        if equipment_type == 'Other':
            cleaned_data['type'] = custom_type
        else:
            cleaned_data['type'] = equipment_type
            
        return cleaned_data
    
class EquipmentExpenseForm(forms.ModelForm):
    class Meta:
        model = EquipmentExpense
        fields = ['date', 'expense_type', 'amount', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }