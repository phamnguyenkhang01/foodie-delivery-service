from rest_framework import serializers
from .models import MenuItem, Restaurant, Order, OrderItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'menu_item', 'quantity', 'price']
        
    def to_internal_value(self, data):
        internal_value = super().to_internal_value(data)
        internal_value['id'] = data.get('id')
        return internal_value
        

class OrderSerializer(serializers.ModelSerializer):
    restaurant = serializers.PrimaryKeyRelatedField(queryset=Restaurant.objects.all())
    order_items = OrderItemSerializer(many=True)
    
    class Meta:
        model = Order
        fields = ['order_id', 'restaurant', 'customer_name', 'customer_address', 'customer_phone', 'status', 'total_price', 'created_at', 'updated_at', 'order_items']
    
    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items')
        order = Order.objects.create(**validated_data)
        
        for item_data in order_items_data:
            OrderItem.objects.create(order=order, **item_data)
            
        return order

class OrderUpdateSerializer (serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['order_id', 'restaurant', 'customer_name', 'customer_address', 'customer_phone', 'status', 'total_price', 'created_at', 'updated_at', 'order_items']
    def update(self, instance, validated_data):
        # Extract nested order_items data
        order_items_data = validated_data.pop('order_items', [])
        
        # Update the main Order fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Update, create, or delete order_items
        existing_items = {item.id: item for item in instance.order_items.all()}  # Get all current items
        received_ids = []

        for item_data in order_items_data:
            item_id = item_data.get('id')  # Check if the item has an ID
            quantity = item_data.get('quantity', 0)  # Get the quantity of the item

            if quantity == 0:  # If quantity is 0, delete the item
                if item_id and item_id in existing_items:
                    print(f"Deleting item with ID {item_id} because quantity is 0")
                    # Ensure the item has a valid ID before deleting
                    existing_items[item_id].delete()
                continue  # Skip further processing for this item

            if item_id and item_id in existing_items:
                # Update existing item
                existing_item = existing_items[item_id]
                for attr, value in item_data.items():
                    setattr(existing_item, attr, value)
                existing_item.save()
                received_ids.append(item_id)
            else:
                # Create a new item
                new_item = OrderItem.objects.create(order=instance, **item_data)
                received_ids.append(new_item.id)

        # Delete items not included in the update request
        for item_id, item in existing_items.items():
            if item_id not in received_ids:
                item.delete()

        return instance

    
class OrderListSerializer(serializers.ModelSerializer):
    restaurant_name = serializers.CharField(source='restaurant.name', read_only=True)
    
    class Meta:
        model = Order
        fields = ['order_id', 'restaurant_name', 'status', 'total_price', 'customer_name']

