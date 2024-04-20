# django_site

[Задание](task.md)

## Установка

1. Создайте `.env` файл и заполните из [примера](env_example):

```bash
touch .env
```

2. Установите зависимости

```bash
pip install -r requirements.txt
```

## Запуск

1. Проведите миграции:

```bash
python3 manage.py migrate
```

2. Создайте суперпользователя:

```bash
python3 manage.py createsuperuser
```

3. Запустите сервер:

```bash
python3 manage.py runserver
```

## Помощь

1. Адрес админки: `http://127.0.0.1:8000/admin/`
2. Адрес сайта: `http://127.0.0.1:8000/`
