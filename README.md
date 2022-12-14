<a name="readme-top">Todolist</a>


This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [![Next][Next.js]][Next-url]
* [![React][React.js]][React-url]
* [![Vue][Vue.js]][Vue-url]
* [![Angular][Angular.io]][Angular-url]
* [![Svelte][Svelte.dev]][Svelte-url]
* [![Laravel][Laravel.com]][Laravel-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JQuery][JQuery.com]][JQuery-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>







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
* SOCIAL_AUTH_VK_OAUTH2_KEY=ключ приложения ВК
* SOCIAL_AUTH_VK_OAUTH2_SECRET=секрет приложения ВК


### Запуск проекта Django:

* Перед запуском проекта, накатываем миграции на базу данных командой

```
python ./manage.py migrate
```
* Запуск проекта

```
python ./manage.py runserver
```
