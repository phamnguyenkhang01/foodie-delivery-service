from menu_item import MenuItem
from restaurant_selector import RestaurantSelector

class Admin:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Admin, cls).__new__(cls)
        return cls._instance
    
    def add_menu_item(self, menu_items):
        print("\nAdding a New Menu Item")
        item_id = len(menu_items) + 1
        name = input("Enter the name of the item: ")
        restaurant_id = int(input("Enter restaurant id of the item: "))
        description = input("Enter the description of the item: ")
        price = float(input("Enter the price of the item: "))
        image_url = input("Enter the image URL for the item: ")
        
        new_item = MenuItem(item_id, restaurant_id, name, description, price, image_url)
        menu_items.append(new_item)
        print(f"\n'{new_item.name}' has been added to the menu")

    def delete_menu_item(self, menu_items):
        print("\nDeleting a Menu Item")
        item_id = int(input("Enter the ID of the item to delete: "))
        item_to_delete = next((item for item in menu_items if item.item_id == item_id), None)
        
        if item_to_delete:
            menu_items.remove(item_to_delete)
            print(f"\n'{item_to_delete.name}' has been deleted from the menu.")
        else:
            print(f"No item found with ID {item_id}.")

    def view_menu(self, restaurants, menu_items):
        restaurant_selector = RestaurantSelector(restaurants)
        restaurant_id = restaurant_selector.select_restaurant()
        
        if restaurant_id:
            print("\nAvailable Menu Items:")
            restaurant_menu = [item for item in menu_items if item.restaurant_id == restaurant_id]
            if restaurant_menu:
                for item in restaurant_menu:
                    print(f"{item.item_id}. {item.name} - ${item.price:.2f} ({item.description})")
            else:
                print("No menu items found for this restaurant.")
    def admin_menu(self, restaurants, menu_items):
        print("\nAdmin Menu")
        while True: 
            print("\n1. Add Menu Item")
            print("2. Delete Menu Item")
            print("3. View Menu")
            print("4. Exit Admin Menu")
            
            choice = input("Enter your choice (1-4): ")
            
            if choice == "1":
                self.add_menu_item(menu_items)
            elif choice == "2":
                self.delete_menu_item(menu_items)
            elif choice == "3":
                    self.view_menu(restaurants, menu_items)
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 4.")