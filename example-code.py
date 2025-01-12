# 1. models.py
from django.db import models

class MenuItem(models.Model):
    restaurant_id = models.IntegerField(default=1)  # Add a default value
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(blank=True)

    def __str__(self):
        return f"id: {self.id}, Restaurant ID: {self.restaurant_id}, Name: {self.name}, Description: {self.description}, Price: {self.price}"



# 2. serializers.py
from rest_framework import serializers
from .models import MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'


# 3. views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MenuItem
from .serializers import MenuItemSerializer

@api_view(['GET'])
def get_menu_items(request):
    restaurant_id = request.query_params.get('restaurant_id')
    if restaurant_id:
        items = MenuItem.objects.filter(restaurant_id=restaurant_id)
    else:
        items = MenuItem.objects.all()
    
    serializer = MenuItemSerializer(items, many=True)
    return Response(serializer.data)


# 4. urls.py
from django.urls import path
from .views import get_menu_items

urlpatterns = [
    path('menu-items/', get_menu_items, name='menu-items'),
]


# 5. settings.py
INSTALLED_APPS = [
    ...,
    'rest_framework',
    'your_app_name',  # Replace with your app name
]


# 6. Run Migrations
# In terminal
python manage.py makemigrations
python manage.py migrate


# 7. Create Test Data
# In terminal
python manage.py shell
from your_app_name.models import MenuItem

MenuItem.objects.create(restaurant_id=1, name="Burger", description="Juicy beef burger", price=5.99)
MenuItem.objects.create(restaurant_id=2, name="Pizza", description="Cheese pizza", price=8.99)
exit()


# 8. Start Server
# In terminal
python manage.py runserver
