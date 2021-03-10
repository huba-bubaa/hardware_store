# Hardware Store - test task
Для начала работы с проектом выполнить следующие действия:
  1. Клонировать проект с репозитория на рабочий компьютер
  2. В консоли открыть папку проекта: ввести следующие команды:
    - python3 -m venv .env
    - . .env/bin/activate
    - pip install -r requirements.txt
    - ./manage.py migrate
    - python3 groups.py - создаем группы для пользователей
    - ./manage.py loaddata products - добавляем записи в таблицу продуктов с помощью фикстуры
    - ./manage.py runserver 
  3. Запускаем Celery:
    - Проверяем, работает ли Редис: redis-cli ping
    - celery -A hardware_store beat -l info
    - celery -A hardware_store worker -l info
  4. Спустя минуту селери должно изменить записи в таблице продуктов
 
  ## ENDPOINTS
  
  ### AUTH
  
  POST: rest-auth/registration/ - регистрация нового User. Поля: 
                                      - email: EmailField
                                      - password1: CharField
                                      - password2: CharField
  
  POST: rest-auth/login/ - вход в аккаунт(получение токена). Поля: 
                                      - email: EmailField
                                      - password: CharField
  
  POST: rest-auth/logout/ - выход из аккаунта(стирает сессию).
  
  GET: rest-auth/user - просмотр профайла пользователя
  
  PUT: rest-auth/user - редактирование пользователя. Поля: 
                                      + email: EmailField
                                      + staff_name: CharField
                                      + groups: Group (shop_assistant, accountant, cashier)
                                      
---
  
  ### Для Cashiers ###
GET, POST: products/ - список продуктов. Поля:  
                                      + product_name: CharField
                                      + price: IntegerField
                                      + delivery_date: DateField ("%y-%m-%d")

GET, PUT: products/<int:id> - продукт по id. Поля:  
                                      + product_name: CharField
                                      + price: IntegerField
                                      + delivery_date: DateField ("%y-%m-%d")

POST, GET: orders/ - список заказов.Поля:  
                                      + product_id: Product (id)
                                      + order_datetime: DateTimeField ("YYY-MM-ddTHH:mm")
                                      + status: CharField(choises): added, paid

POST, GET: orders/ - список заказов.Поля:  
                                      + product_id: Product (id)
                                      + order_datetime: DateTimeField ("YYY-MM-ddTHH:mm")
                                      + status: CharField(choises): added, paid
