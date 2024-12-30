from restaurant import Restaurant

class RestaurantSelector:
    def __init__(self, restaurants):
        self.restaurants = restaurants
    
    def select_restaurant(self):
        print("\nAvailable Restaurants:")
        for restaurant in self.restaurants:
            print(f"{restaurant.restaurant_id}. {restaurant.name} - {restaurant.address}")
        try:
            restaurant_id = int (input("Enter the ID of the restaurant you want to browse: "))
            selected_restaurant = next((r for r in self.restaurants if r.restaurant_id == restaurant_id), None)
            if selected_restaurant:
                print(f"\nWelcome to {selected_restaurant.name}!")
                return restaurant_id
            else:
                print("Invalid restaurant ID. Please try again.")
                return None
        except ValueError:
            print("Invalid input. Please enter a valid restaurant ID.")
            return None