from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import MenuItem, Restaurant, Order, OrderItem
from .serializers import MenuItemSerializer, RestaurantSerializer, OrderItemSerializer, OrderSerializer, OrderListSerializer, OrderUpdateSerializer

# Get all menu items
@api_view(['GET'])
def get_menu_items(request):
    restaurant_id = request.query_params.get('restaurant_id')
    if restaurant_id:
        items = MenuItem.objects.filter(restaurant_id=restaurant_id)
    else:
        items = MenuItem.objects.all()
    
    serializer = MenuItemSerializer(items, many=True)
    return Response(serializer.data)

# Get a menu item
@api_view(['GET'])
def get_menu_item(request, pk):
    try:
        item = MenuItem.objects.get(pk=pk)
    except MenuItem.DoesNotExist:
        return Response({'error': 'Menu item not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = MenuItemSerializer(item)
    return Response(serializer.data)

# Create a menu item
@api_view(['POST'])
def add_menu_item(request):
    if request.method == 'POST':
        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# delete a menu item
@api_view(['DELETE'])
def delete_menu_item(request, pk):
    try:
        item = MenuItem.objects.get(pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except MenuItem.DoesNotExist:
        return Response({'error': 'Menu item not found'}, status=status.HTTP_404_NOT_FOUND)

# update a menu item
@api_view(['PUT'])
def update_menu_item(request, pk):
    try:
        item = MenuItem.objects.get(pk=pk)
    except MenuItem.DoesNotExist:
        return Response({'error': 'Menu item not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = MenuItemSerializer(item, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#get all restaurant
@api_view(['GET'])
def get_all_restaurants(request):
    restaurants = Restaurant.objects.all()
    serializer = RestaurantSerializer(restaurants, many=True)
    return Response(serializer.data)

# get a restaurant
@api_view(['GET'])
def get_restaurant_and_menu(request, pk):
    try:
        restaurant = Restaurant.objects.get(pk=pk)
        menu_items = MenuItem.objects.filter(restaurant_id=restaurant)
    except Restaurant.DoesNotExist:
        return Response({'error': 'Restaurant not found'}, status=status.HTTP_404_NOT_FOUND)
    
    restaurant_serializer = RestaurantSerializer(restaurant)
    menu_items_serializer = MenuItemSerializer(menu_items, many=True)
    
    return Response({
        'restaurant': restaurant_serializer.data,
        'menu_items': menu_items_serializer.data
    })

# Create Restaurant
@api_view(['GET'])
def add_restaurant(request):
    serializer = RestaurantSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete a Restaurant
@api_view(['DELETE'])
def delete_restaurant(request, pk):
    try:
        restaurant = Restaurant.objects.get(pk=pk)
        restaurant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Restaurant.DoesNotExist:
        return Response({'error': 'Restaurant not found'}, status=status.HTTP_404_NOT_FOUND)

# Update a Restaurant
@api_view(['PUT'])
def update_restaurant(request, pk):
    try:
        restaurant = Restaurant.objects.get(pk=pk)
    except Restaurant.DoesNotExist:
        return Response({'error': 'Restaurant not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = RestaurantSerializer(restaurant, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Get Orders
@api_view(['GET'])
def get_all_orders(request):
    orders = Order.objects.all()
    serializer = OrderListSerializer(orders, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Get an order
@api_view(['GET'])
def get_order(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
    

# Create an order
@api_view(['POST'])
def create_order(request):
    if request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Delete an order
@api_view(['DELETE'])
def delete_order(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
        order.delete()
        return Response({"message": "Order deleted sucessfully"}, status=status.HTTP_204_NO_CONTENT)
    except Order.DoesNotExist:
        return Response({"error": "Order not found."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT', 'PATCH'])
def update_order(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
    
    except Order.DoesNotExist:
        return Response({"error": "Order not found."}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = OrderUpdateSerializer(order, data=request.data)
    # elif request.method == 'PATCH':
    #     serializer = OrderUpdateSerializer(order, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        


    
        

