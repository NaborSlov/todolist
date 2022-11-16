# Todolist

Планировщик задач который позволяет работать с целями и отслеживанием прогресса по ним.

### В проекте используется

Django==4.0.1

### Перед началом работы:

#### Установка зависимостей:

В корневой папке находиться файл с зависимостями requirements.txt 

#### Развертывание базы данных:

Для удобства развертывания базы данных в папке postgresql находиться файл docker-compose 

#### Настройка переменных окружения:

Для работы проекта необходимо создать **.env** в корневой папке.
В нем нужно указать необходимые значения переменных:

* DEBUG=True (или False) - включения или выключения дебагера django
* SECRET_KEY=*секретный ключ*
* DATABASE_URL=psql://<имя пользователя>:<пароль пользователя>@<ip адрес>:<порт>/<имя базы>

### Запуск проекта Django:

* Перед запуском проекта, накатываем миграции на базу данных командой

```
python ./manage.py migrate
```
* Запуск проекта

```
python ./manage.py runserver
```
