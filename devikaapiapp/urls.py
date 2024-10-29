from django.urls import path
from devikaapiapp import views

urlpatterns = [
    path('item_list/',views.item_list,name='item_list'),
    path('list_item/<int:pk>/',views.list_item,name='list_item')
 
]