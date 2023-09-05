from django.contrib import admin
from django.urls import path, include
from . import views
from .views import TestCRUD
import debug_toolbar


urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),  # Fixed quotes
    path('add_inventory/<int:item_id>/', views.add_item, name='add_item'),
    path('', views.item_list, name='item_list'),
    path('edit/<int:pk>/', views.edit_item, name='edit_item'),
    path('delete/<int:pk>/', views.delete_item, name='delete_item'),
    path('test_crud/', TestCRUD.as_view(), name='test_crud'),
]
