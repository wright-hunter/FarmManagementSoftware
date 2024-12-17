from django.urls import path
from . import views

urlpatterns = [
    path('equipment/', views.equipment_list, name='equipment_list'),
    path('equipment/add/', views.add_equipment, name='add_equipment'),
    path('equipment/<int:equipment_id>/edit/', views.edit_equipment, name='edit_equipment'),
    path('equipment/<int:equipment_id>/delete/', views.delete_equipment, name='delete_equipment'),
    path('<int:equipment_id>/history/', views.equipment_history, name='equipment_history'),
    path('<int:equipment_id>/add-expense/', views.add_expense, name='add_equipment_expense'),
    path('<int:equipment_id>/expense/<int:expense_id>/edit/', views.edit_expense, name='edit_equipment_expense'),
    path('equipment/<int:equipment_id>/expense/<int:expense_id>/delete/', views.delete_expense, name='delete_equipment_expense'),
]