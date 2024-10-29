from rest_framework import serializers
from .models import Item

class item_serializer(serializers.ModelSerializer):
    class Meta:
        model = Item 
        fields = ['id','name','description']