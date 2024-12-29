from menu import MenuItem

menu_items = [
    MenuItem(1, 101, 'Cheeseburger', 'Juicy beef patty with cheese', 5.99, 'https://example.com/images/cheeseburger.jpg'),
    MenuItem(2, 101, 'Veggie Pizza', 'Delicious pizza with fresh vegetables', 8.99, 'https://example.com/images/veggie-pizza.jpg'),
    MenuItem(3, 102, 'Chicken Sandwich', 'Grilled chicken with lettuce and mayo', 6.49, 'https://example.com/images/chicken-sandwich.jpg'),
    MenuItem(4, 103, 'Pasta', 'Pasta with tomato sauce and basil', 7.99, 'https://example.com/images/pasta.jpg')
]

order_history = []  # List to store order history

def display_menu():
    print("\nAvailable Menu Items:")
    for item in menu_items:
        print(f"{item.item_id}. {item.name} - ${item.price:.2f} ({item.description})")

def search_menu_item(query):
    print(f"\nSearch results for '{query}':")
    results = [item for item in menu_items if query.lower() in item.name.lower()]
    if results:
        for item in results:
            print(f"{item.item_id}. {item.name} - ${item.price:.2f} ({item.description})")
    else:
        print("No items found matching your search.")

def place_order(order_ids):
    order_total = 0
    order_details = []  # To store details of the current order
    print("\nYour Order Summary: ")
    
    for order_id in order_ids:
        item = next((item for item in menu_items if item.item_id == order_id), None)
        if item:
            print(f"{item.name} - ${item.price:.2f}")
            order_details.append(f"{item.name} - ${item.price:.2f}")
            order_total += item.price
        else:
            print(f"Item with ID {order_id} not found.")
    
    print(f"Total Amount: ${order_total:.2f}")
    
    # Add the current order to the order history
    order_history.append({
        'items': order_details,
        'total': order_total
    })
    
    print("\nOrder has been placed and added to order history.")

def view_order_history():
    if order_history:
        print("\nOrder History:")
        for index, order in enumerate(order_history, start=1):
            print(f"\nOrder {index}:")
            for item in order['items']:
                print(f"- {item}")
            print(f"Total: ${order['total']:.2f}")
    else:
        print("\nNo orders placed yet.")

# Admin functions
def add_menu_item():
    print("\nAdding a New Menu Item")
    item_id = len(menu_items) + 1  # Automatically generate a new ID based on the list length
    name = input("Enter the name of the item: ")
    description = input("Enter the description of the item: ")
    price = float(input("Enter the price of the item: "))
    image_url = input("Enter the image URL for the item: ")
    category_id = int(input("Enter the category ID (e.g., 101 for burgers): "))
    
    new_item = MenuItem(item_id, category_id, name, description, price, image_url)
    menu_items.append(new_item)
    print(f"\n'{new_item.name}' has been added to the menu.")

def delete_menu_item():
    print("\nDeleting a Menu Item")
    item_id = int(input("Enter the ID of the item to delete: "))
    item_to_delete = next((item for item in menu_items if item.item_id == item_id), None)
    
    if item_to_delete:
        menu_items.remove(item_to_delete)
        print(f"\n'{item_to_delete.name}' has been deleted from the menu.")
    else:
        print(f"No item found with ID {item_id}.")

def admin_menu():
    while True:
        print("\nAdmin Menu")
        print("1. Add Menu Item")
        print("2. Delete Menu Item")
        print("3. View Menu")
        print("4. Exit Admin Menu")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            add_menu_item()
        elif choice == "2":
            delete_menu_item()
        elif choice == "3":
            display_menu()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

def main():
    while True:
        print("\nWelcome to the Food Delivery App")
        print("1. View Menu")
        print("2. Search Menu Item")
        print("3. Place an Order")
        print("4. View Order History")
        print("5. Admin Menu (For Admin Users)")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            display_menu()
        elif choice == "2":
            query = input("Enter the name of the item to search: ")
            search_menu_item(query)
        elif choice == "3":
            display_menu()
            order_ids = input("Enter the item IDs you want to order (comma-separated): ")
            try:
                order_ids = list(map(int, order_ids.split(',')))
                place_order(order_ids)
            except ValueError:
                print("Invalid input. Please enter valid item IDs separated by commas.")
        elif choice == "4":
            view_order_history()
        elif choice == "5":
            admin_menu()  # Admin menu to manage menu items
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
