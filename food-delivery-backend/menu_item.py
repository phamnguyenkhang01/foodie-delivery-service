# menu_item.py

class MenuItem:
    def __init__(self, item_id, restaurant_id, name, description, price, image_url):
        self.item_id = item_id
        self.restaurant_id = restaurant_id
        self.name = name
        self.description = description
        self.price = price
        self.image_url = image_url

    def __repr__(self):
        return f"MenuItem({self.item_id}, {self.restaurant_id}, '{self.name}', '{self.description}', {self.price}, '{self.image_url}')"
