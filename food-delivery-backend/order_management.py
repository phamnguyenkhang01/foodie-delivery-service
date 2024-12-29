from menu_item import MenuItem

class OrderManagement:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OrderManagement, cls).__new__(cls)
        return cls._instance
    
    
    def place_order(self, order_ids, menu_items, order_history):
        order_total = 0
        order_details = []
        for order_id in order_ids:
            item = next((item for item in menu_items if item.item_id== order_id), None)
            if item:
                order_details.append(f"{item.name} - ${item.price:.2f}")
                order_total += item.price
        order_history.append({'items': order_details, 'total': order_total})
        return order_total, order_details
    
    def view_order_history(self, order_history):
        if order_history:
            return "\n".join([f"Order {i+1}: {', '.join(order['items'])} - Total: ${order['total']:.2f}" for i, order in enumerate(order_history)])
        else:
            return("\nNo orders placed yet.")
    
    def search_menu_item(self, query, menu_items):
        results = [item for item in menu_items if query.lower() in item.name.lower()]
        return results