from admin import Admin
from menu_item import MenuItem
from restaurant import Restaurant
from order_management import OrderManagement
from restaurant_selector import RestaurantSelector

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

order_management = OrderManagement()

select_restaurant = RestaurantSelector(restaurants)

admin = Admin()

def main_menu():
        print("\nWelcome to the Food Delivery App")
        print("1. Select Restaurant and View Menu")
        print("2. Search Menu Item")
        print("3. Place an Order")
        print("4. View Order History") 
        print("5. Admin Menu(For Admin Users)")
        print("9. Exit")
        return input("Enter your choice (1-9): ")
    

def main():    
    while True:
        choice = main_menu()
        if choice == "1":
                admin.view_menu(restaurants, menu_items)
        elif choice == "2":
            order_management.search_menu_item(menu_items)
                
        elif choice == "3":
            order_management.place_order(menu_items, restaurants)
                    
        elif choice == "4":
            order_management.view_order_history()
            
        elif choice == "5":
            admin.admin_menu(restaurants, menu_items)
        
        elif choice == "9":
            print("Thank you for using the Food Delivery App. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()