from django.db import models
from django.utils import timezone

class Restaurant(models.Model):
    restaurant_id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    
    def __str__(self):
        return f"Restaurant(id: {self.restaurant_id}, name: {self.name}, address: {self.address})"

class MenuItem(models.Model):
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)  # Add a default value
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(blank=True)

    def __str__(self):
        return f"id: {self.id}, Restaurant ID: {self.restaurant_id}, Name: {self.name}, Description: {self.description}, Price: {self.price}"

class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]
    
    order_id = models.AutoField(primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='orders')
    menu_items = models.ManyToManyField(MenuItem, through='OrderItem')
    customer_name = models.CharField(max_length=100)
    customer_address = models.CharField(max_length=255)
    customer_phone = models.CharField(max_length=15)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='PENDING')
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        order_items = self.order_items.all().order_by('id')
        menu_items_str = '\n'.join([f"id: {order_item.id} - {order_item.menu_item.name}(id: {order_item.menu_item.id}) - quantity: {order_item.quantity}" for order_item in order_items])
        return f"Order(id: {self.order_id}, Restaurant: {self.restaurant.name}, Status: {self.status}, Menu Items: \n{menu_items_str}"
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return f"OrderItem(Order ID: {self.order.order_id}, MenuItem: {self.menu_item.name}, Quantity: {self.quantity}, Price: {self.price})"

