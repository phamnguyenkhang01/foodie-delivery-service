cd food-delivery-backend
.\venv\Scripts\Activate
cd food_delivery
python manage.py runserver

cd food-delivery-frontend
npm start

python main.py





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

1. Add thêm image vào restaurant trong database
