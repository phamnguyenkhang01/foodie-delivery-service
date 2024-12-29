#restaurant.py

class Restaurant:
    def __init__(self, restaurant_id, name, address):
        self.restaurant_id = restaurant_id
        self.name = name
        self.address = address
    def __repr__(self):
        return f"Restaurant({self.restaurant_id}, '{self.name}', '{self.address}')"