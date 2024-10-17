# serializers.py
from rest_framework import serializers
from .models import Customer, Product, Inventory
# Serializer for the Customer model
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'country', 'registration_date']

# Serializer for the Product model
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
# Serializer for updating the inventory        
class InventoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['quantity']  # Ensure 'inventory' field exists in your Product model

    def validate_inventory(self, value):
        if value < 0:
            raise serializers.ValidationError("Inventory level cannot be negative.")
        return value        