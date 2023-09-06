from django.contrib import admin
from django.urls import path, include
from . import views

import debug_toolbar


urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('', views.Inventory, name='Home'),
    path('add_items/', views.add_items, name='add_items'),
    path('edit_item/', views.edit_item, name='edit_item'),
    path('item_list/', views.item_list, name='item_list'),

]
