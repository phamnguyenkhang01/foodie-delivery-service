CREATE TABLE MenuItem (
    id INT AUTO_INCREMENT PRIMARY KEY,
    restaurant_id INT DEFAULT 1,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(6, 2),
    image_url VARCHAR(255)
);

INSERT INTO MenuItem (restaurant_id, name, description, price, image_url)
VALUES
(101, 'Cheeseburger', 'Juicy beef patty with cheese', 5.99, 'https://example.com/images/cheeseburger.jpg'),
(101, 'Veggie Pizza', 'Delicious pizza with fresh vegetables', 8.99, 'https://example.com/images/veggie-pizza.jpg'),
(102, 'Chicken Sandwich', 'Grilled chicken with lettuce and mayo', 6.49, 'https://example.com/images/chicken-sandwich.jpg'),
(103, 'Pasta', 'Pasta with tomato sauce and basil', 7.99, 'https://example.com/images/pasta.jpg');