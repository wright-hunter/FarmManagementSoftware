from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Field, YearlyFieldData
from .forms import FieldForm, YearlyFieldDataForm
from django.db.models import Q  # For advanced filtering

def field_list(request):
    query = request.GET.get('q', '')  # Get the search term from the query string
    location = request.GET.get('location', '')  # Get the location filter from the query string

    # Base queryset
    fields = Field.objects.all()

    # Apply filters
    if query:
        fields = fields.filter(Q(name__icontains=query))
    if location:
        fields = fields.filter(location=location)

    # Pass filters back to the template
    locations = Field.objects.values_list('location', flat=True).distinct()
    return render(request, 'fields/field_list.html', {
        'fields': fields,
        'query': query,
        'locations': locations,
        'selected_location': location,
    })


def add_field(request):
    if request.method == 'POST':
        form = FieldForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('field_list')
    else:
        form = FieldForm()
    return render(request, 'fields/add_field.html', {'form': form})

def edit_field(request, field_id):
    field = get_object_or_404(Field, pk=field_id)
    if request.method == 'POST':
        form = FieldForm(request.POST, instance=field)
        if form.is_valid():
            form.save()
            return redirect('field_list')
    else:
        form = FieldForm(instance=field)
    return render(request, 'fields/edit_field.html', {'form': form, 'field': field})

def delete_field(request, field_id):
    field = get_object_or_404(Field, id=field_id)
    field.delete()
    return redirect('field_list')

def field_history(request, field_id):
    field = get_object_or_404(Field, id=field_id)
    yearly_data = field.yearly_data.all()
    return render(request, 'fields/field_history.html', {
        'field': field,
        'yearly_data': yearly_data
    })

def add_yearly_data(request, field_id):
    field = get_object_or_404(Field, pk=field_id)
    if request.method == 'POST':
        form = YearlyFieldDataForm(request.POST, field=field)  # Add field here
        if form.is_valid():
            yearly_data = form.save(commit=False)
            yearly_data.field = field
            if form.cleaned_data['crop'] == 'Other':
                yearly_data.crop = form.cleaned_data['custom_crop']
            yearly_data.save()
            return redirect('field_history', field_id=field.id)
    else:
        form = YearlyFieldDataForm(field=field)  # Add field here
    return render(request, 'fields/add_yearly_data.html', {'form': form, 'field': field})

def edit_yearly_data(request, field_id, data_id):
    field = get_object_or_404(Field, pk=field_id)
    yearly_data = get_object_or_404(YearlyFieldData, pk=data_id)
    if request.method == 'POST':
        form = YearlyFieldDataForm(request.POST, instance=yearly_data)
        if form.is_valid():
            yearly_data = form.save(commit=False)
            if form.cleaned_data['crop'] == 'Other':
                yearly_data.crop = form.cleaned_data['custom_crop']
            yearly_data.save()
            return redirect('field_history', field_id=field.id)
    else:
        form = YearlyFieldDataForm(instance=yearly_data)
    return render(request, 'fields/edit_yearly_data.html', {
        'form': form,
        'field': field,
        'yearly_data': yearly_data
    })

def delete_yearly_data(request, data_id):
    yearly_data = get_object_or_404(YearlyFieldData, id=data_id)
    field_id = yearly_data.field.id
    yearly_data.delete()
    return redirect('field_history', field_id=field_id)