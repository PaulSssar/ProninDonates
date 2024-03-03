# ProninDonates
Приложение ProninDonates создано для создания сборов донатов.

## Шаблон описания файла .env
- DB_ENGINE=django.db.backends.postgresql
- POSTGRES_DB=<база данных postgres>
- POSTGRES_USER=<пользователь postgres>
- POSTGRES_PASSWORD=<пароль postgres>
- DB_HOST=<хост postgres>
- DB_PORT=<порт postgres>
- DEBUG=<режим отладки>

## Наполнение базы mock-данными
### Для наполнения базы данных, необходимо:
- Добавить пользователей командой
```bash
python manage.py add_users <count>
```
- Добавить причины сбора командой
```bash
python manage.py add_occasions <count>
```
- Добавить сборы командой
```bash
python manage.py add_collects <count>
```
- Добавить платежи командой
```bash
python manage.py add_payments <count>
```
count - количество записей

### Инструкции для развертывания и запуска приложения
для Linux-систем все команды необходимо выполнять от имени администратора1
- Склонировать репозиторий
```bash
git clone https://github.com/paulsssar/ProninDonates.git
```
- Выполнить вход на удаленный сервер
- Установить docker на сервер:
```bash
apt install docker.io 
```
- Установить docker-compose на сервер:
```bash
apt install docker-compose
```

- Скопировать файлы docker-compose.yml и default.conf на сервер:
```bash
scp docker-compose.yml <username>@<host>:/home/<username>/docker-compose.yml
scp default.conf <username>@<host>:/home/<username>/nginx/nginx.conf
```
- Создать .env файл по предлагаемому выше шаблону.

- собрать и запустить контейнеры на сервере:
```bash
docker-compose up -d --build
```
- После успешной сборки выполнить следующие действия (только при первом деплое):
    ```  
    * Создать суперпользователя Django, после запроса от терминала ввести логин и пароль для суперпользователя:
    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```

## Автор
Павел Сарыгин 