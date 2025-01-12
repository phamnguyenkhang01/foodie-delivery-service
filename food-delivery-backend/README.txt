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






1. Fix Order Create: Price nên link giữa Order Item model và MenuItem model, tính tiền bằng công thức không phải hardcode
2. Order Update: chưa làm được test case: update một id có sẵn thi nó lại xóa id đó, tạo id mới. delete bằng cách chuyển quantity về bằng 0