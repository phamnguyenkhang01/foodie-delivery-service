from menu_item import MenuItem
from restaurant_selector import RestaurantSelector

class OrderManagement:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OrderManagement, cls).__new__(cls)
            cls._instance.order_history = []
        return cls._instance
    
    
    def place_order(self, menu_items, restaurants):
        restaurant_selector = RestaurantSelector(restaurants)
        restaurant_id = restaurant_selector.select_restaurant()
        if restaurant_id:
            order_ids = input("Enter the item IDs to order (comma-separated): ")
            try:
                order_ids = list(map(int, order_ids.split(',')))
                order_total = 0
                order_details = []
                for order_id in order_ids:
                    item = next((item for item in menu_items if item.item_id== order_id), None)
                    if item:
                        order_details.append(f"{item.name} - ${item.price:.2f}")
                        order_total += item.price
                self.order_history.append({'items': order_details, 'total': order_total})
                print(f"\nYour order has been placed. Total: ${order_total:.2f}")
                print("Order Details:")
                for detail in order_details:
                    print(f"- {detail}")
            except ValueError:
                    print("Invalid input. Please enter valid item IDs seperated by commas.")
    
    def view_order_history(self):
        print("\nOrder History:")
        if self.order_history:
            print ("\n".join([f"Order {i+1}: {', '.join(order['items'])} - Total: ${order['total']:.2f}" for i, order in enumerate(self.order_history)]))
        else:
            print("\nNo orders placed yet.")
    
    def search_menu_item(self, menu_items):
        query= input("Enter the name of the item to search: ")
        results = [item for item in menu_items if query.lower() in item.name.lower()]
        if True:
            print("\nSearch Results:")
            for item in results:
                print (f"{item.item_id}. {item.name} - ${item.price:.2f}")
        else:
            print ("No items found.")