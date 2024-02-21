```###Древовидное меню, добавление на url указанных меню через админку. У каждого меню есть url (можно указать кастомный через админку). ###```

Все для тестов создал на базовом url, запускайте, смотрите :3

Клонировать:
```
git clone https://github.com/justmedic/UpTrader
```

Виртуальное окружение (если нужно):
```
python -m venv env
```
```
env\scripts\activate
```
Установка зависимостей:
```
pip install -r requirements.txt
```
Миграции:
```
python manage.py migrate
```
Создание админа:
```
python manage.py createsuperuser
```
Запуск:
```
python manage.py runserver
```
