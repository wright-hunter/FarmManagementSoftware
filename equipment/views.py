from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipment, EquipmentExpense
from .forms import EquipmentForm, EquipmentExpenseForm
from django.db.models import Q

def add_equipment(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            equipment = form.save(commit=False)
            equipment.type = form.cleaned_data['type']
            equipment.save()
            return redirect('equipment_list')
    else:
        form = EquipmentForm()
    return render(request, 'equipment/add_equipment.html', {'form': form})

def edit_equipment(request, equipment_id):
    equipment = get_object_or_404(Equipment, pk=equipment_id)
    if request.method == 'POST':
        form = EquipmentForm(request.POST, instance=equipment)
        if form.is_valid():
            equipment = form.save(commit=False)
            equipment.type = form.cleaned_data['type']
            equipment.save()
            return redirect('equipment_list')
    else:
        # Pre-fill the form with existing equipment data
        initial_data = {
            'equipment_type': equipment.type,
            'custom_type': equipment.type if equipment.type not in dict(EquipmentForm.EQUIPMENT_TYPES).keys() else '',
        }
        form = EquipmentForm(instance=equipment, initial=initial_data)
    return render(request, 'equipment/edit_equipment.html', {
        'form': form,
        'equipment': equipment
    })

def equipment_list(request):
    query = request.GET.get('q', '')
    equipment_type = request.GET.get('type', '')

    equipment = Equipment.objects.all()

    if query:
        equipment = equipment.filter(
            Q(make__icontains=query) | 
            Q(model__icontains=query)
        )
    if equipment_type:
        equipment = equipment.filter(type=equipment_type)

    types = EquipmentForm.EQUIPMENT_TYPES
    return render(request, 'equipment/equipment_list.html', {
        'equipment': equipment,
        'query': query,
        'types': types,
        'selected_type': equipment_type,
    })

def delete_equipment(request, equipment_id):
    equipment = get_object_or_404(Equipment, id=equipment_id)
    equipment.delete()
    return redirect('equipment_list')

def equipment_history(request, equipment_id):
    equipment = get_object_or_404(Equipment, id=equipment_id)
    expenses = equipment.expenses.all()
    return render(request, 'equipment/equipment_history.html', {
        'equipment': equipment,
        'expenses': expenses
    })

def add_expense(request, equipment_id):
    equipment = get_object_or_404(Equipment, id=equipment_id)
    if request.method == 'POST':
        form = EquipmentExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.equipment = equipment
            expense.save()
            return redirect('equipment_history', equipment_id=equipment_id)
    else:
        form = EquipmentExpenseForm()
    return render(request, 'equipment/add_expense.html', {
        'form': form,
        'equipment': equipment
    })

def edit_expense(request, equipment_id, expense_id):
    equipment = get_object_or_404(Equipment, pk=equipment_id)
    expense = get_object_or_404(EquipmentExpense, pk=expense_id, equipment=equipment)
    
    if request.method == 'POST':
        form = EquipmentExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.equipment = equipment
            expense.save()
            return redirect('equipment_history', equipment_id=equipment_id)
    else:
        form = EquipmentExpenseForm(instance=expense)
    
    return render(request, 'equipment/edit_expense.html', {
        'form': form,
        'equipment': equipment,
        'expense': expense
    })
    
def delete_expense(request, equipment_id, expense_id):
    equipment = get_object_or_404(Equipment, pk=equipment_id)
    expense = get_object_or_404(EquipmentExpense, pk=expense_id, equipment=equipment)
    expense.delete()
    return redirect('equipment_history', equipment_id=equipment_id)