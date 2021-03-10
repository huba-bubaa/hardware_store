# Hardware Store - test task
Для начала работы с проектом выполнить следующие действия:
  1. Клонировать проект с репозитория на рабочий компьютер
  2. В консоли открыть папку проекта: ввести следующие команды:
    2.1 python3 -m venv .env
    2.2 . .env/bin/activate
    2.3 pip install -r requirements.txt
    2.4 ./manage.py migrate
    2.5 python3 groups.py - создаем группы для пользователей
    2.6 ./manage.py loaddata products - добавляем записи в таблицу продуктов с помощью фикстуры
    2.7 ./manage.py runserver 
  3. Запускаем Celery:
    3.1 Проверяем, работает ли Редис: redis-cli ping
    3.2 celery -A hardware_store beat -l info
    3.3 celery -A hardware_store worker -l info
  4. Спустя минуту селери должно изменить записи в таблице продуктов
  
  ## ENDPOINTS
