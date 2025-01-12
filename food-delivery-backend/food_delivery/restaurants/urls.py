from django.urls import path
from .views import get_menu_items, get_menu_item, add_menu_item, delete_menu_item, update_menu_item, get_all_restaurants, get_restaurant_and_menu, add_restaurant, delete_restaurant, update_restaurant
from .views import get_all_orders, get_order, create_order, delete_order, update_order

urlpatterns = [
    # Menu_items
    path('menu-items/getall/', get_menu_items, name='menu-items'),
    path('menu-items/get/<int:pk>/', get_menu_item, name='menu-item'),
    path('menu-items/add/', add_menu_item, name='add-menu-item'),
    path('menu-items/delete/<int:pk>', delete_menu_item, name='delete-menu-item'),
    path('menu-items/update/<int:pk>/', update_menu_item, name='update'),
    
    # Restaurants
    path('getall/', get_all_restaurants, name='get_all_restaurants'),
    path('get/<int:pk>/', get_restaurant_and_menu, name="get-restaurant-and-menu"),
    path('add/', add_restaurant, name='add-restaurant'),
    path('delete/<int:pk>/', delete_restaurant, name='delete_restaurant'),
    path('update/<int:pk>/', update_restaurant, name='update_restaurant'),
    
    # Orders
    path('orders/', get_all_orders, name='order-list'),
    path('orders/<int:order_id>/', get_order, name='get_order'),
    path('orders/add/', create_order, name='order-create'),
    path('orders/delete/<int:order_id>/', delete_order, name='order-delete'),
    path('orders/update/<int:order_id>/', update_order, name='order-update'),
]