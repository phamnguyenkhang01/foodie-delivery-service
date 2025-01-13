.\venv\Scripts\Activate
cd food_delivery

python main.py

python manage.py runserver



python manage.py makemigrations
python manage.py migrate

python manage.py shell


from restaurants.models import MenuItem

menu_items = MenuItem.objects.all()
for item in menu_items:
    print(item)

orders = Order.objects.all()
for order in orders:
    print(order)

// Clear database:
python manage.py flush 
