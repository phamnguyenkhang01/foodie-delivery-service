from admin import Admin
from menu_item import MenuItem
from restaurant import Restaurant
from order_management import OrderManagement

restaurants = [
    Restaurant(101, 'Burger Palace', '123 Burger St'),
    Restaurant(102, 'Pizza Paradise', '456 Pizza Ave'),
    Restaurant(103, 'Pasta Heaven', '789 Pasta Blvd')
]

menu_items = [
    MenuItem(1, 101, 'Cheeseburger', 'Juicy beef patty with cheese', 5.99, 'https://example.com/images/cheeseburger.jpg'),
    MenuItem(2, 101, 'Veggie Pizza', 'Delicious pizza with fresh vegetables', 8.99, 'https://example.com/images/veggie-pizza.jpg'),
    MenuItem(3, 102, 'Chicken Sandwich', 'Grilled chicken with lettuce and mayo', 6.49, 'https://example.com/images/chicken-sandwich.jpg'),
    MenuItem(4, 103, 'Pasta', 'Pasta with tomato sauce and basil', 7.99, 'https://example.com/images/pasta.jpg')
]

order_history = []

order_management = OrderManagement()

def delete_menu_item():
    print("\nDeleting a Menu Item")
    item_id = int(input("Enter the ID of the item to delete: "))
    item_to_delete = next((item for item in menu_items if item.item_id == item_id), None)
    
    if item_to_delete:
        menu_items.remove(item_to_delete)
        print(f"\n'{item_to_delete.name}' has been deleted from the menu.")
    else:
        print(f"No item found with ID {item_id}.")


def display_restaurant():
    print("\nAvailable Restaurants:")
    for restaurant in restaurants:
        print(f"{restaurant.restaurant_id}. {restaurant.name} - {restaurant.address}")

def select_restaurant():
    display_restaurant()
    try:
        restaurant_id = int (input("Enter the ID of the restaurant you want to browse: "))
        selected_restaurant = next((r for r in restaurants if r.restaurant_id == restaurant_id), None)
        if selected_restaurant:
            print(f"\nWelcome to {selected_restaurant.name}!")
            return restaurant_id
        else:
            print("Invalid restaurant ID. Please try again.")
            return None
    except ValueError:
        print("Invalid input. Please enter a valid restaurant ID.")
        return None


def main():
    admin = Admin()
    
    while True:
        print("\nWelcome to the Food Delivery App")
        print("1. Select Restaurant and View Menu")
        print("2. Search Menu Item")
        print("3. Place an Order")
        print("4. View Order History") 
        print("5. Admin Menu(For Admin Users)")
        print("9. Exit")
        
        choice = input("Enter your choice (1-9): ")
        
        if choice == "1":
            restaurant_id = select_restaurant()
            if restaurant_id:
                admin.view_menu(restaurant_id, menu_items)
        elif choice == "2":
            query= input("Enter the name of the item to search: ")
            search_results= order_management.search_menu_item(query, menu_items)
            if search_results:
                print("\nSearch Results:")
                for item in search_results:
                    print(f"{item.item_id}. {item.name} - ${item.price:.2f}")
            else:
                print("No items found.")
                
        elif choice == "3":
            restaurant_id = select_restaurant()
            if restaurant_id:
                order_ids = input("Enter the item IDs to order (comma-seperated): ")
                try:
                    order_ids = list(map(int, order_ids.split(',')))
                    total, order_details = order_management.place_order(order_ids, menu_items, order_history)
                    print(f"\nYour order has been placed. Total: ${total:.2f}")
                    print("Order Details:")
                    for detail in order_details:
                        print(f"- {detail}")
                except ValueError:
                    print("Invalid input. Please enter valid item IDs seperated by commas.")
                    
        elif choice == "4":
            print("\nOrder History:")
            print(order_management.view_order_history(order_history))
            
        elif choice == "5":
                print("\nAdmin Menu")
                while True: 
                    print("1. Add Menu Item")
                    print("2. Delete Menu Item")
                    print("3. View Menu")
                    print("4. Exit Admin Menu")
                    
                    choice = input("Enter your choice (1-4): ")
                    
                    if choice == "1":
                        admin.add_menu_item(menu_items)
                    elif choice == "2":
                        admin.delete_menu_item(menu_items)
                    elif choice == "3":
                        restaurant_id = select_restaurant()
                        if restaurant_id:
                            admin.view_menu(restaurant_id, menu_items)
                    elif choice == "4":
                        break
                    else:
                        print("Invalid choice. Please enter a number from 1 to 4.")
        
        elif choice == "9":
            print("Thank you for using the Food Delivery App. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()