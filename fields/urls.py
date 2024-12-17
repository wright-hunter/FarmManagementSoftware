from django.urls import path
from . import views

urlpatterns = [
    # Field-related URLs
    path('fields/', views.field_list, name='field_list'),
    path('fields/add/', views.add_field, name='add_field'),
    path('fields/<int:field_id>/', views.field_history, name='field_history'),
    path('fields/<int:field_id>/edit/', views.edit_field, name='edit_field'),
    path('fields/<int:field_id>/delete/', views.delete_field, name='delete_field'),
    
    # Yearly data-related URLs
    path('fields/<int:field_id>/yearly-data/add/', views.add_yearly_data, name='add_yearly_data'),
    path('fields/<int:field_id>/yearly-data/<int:data_id>/edit/', views.edit_yearly_data, name='edit_yearly_data'),
    path('fields/<int:field_id>/yearly-data/<int:data_id>/delete/', views.delete_yearly_data, name='delete_yearly_data'),
]