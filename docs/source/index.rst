GraphQL API Gateway
===================

Пример реализации GraphQL API шлюза для взаимодействия с микросервисами.

Зависимости
===========
1. Docker для контейнеризации – |link_docker|

.. |link_docker| raw:: html

   <a href="https://www.docker.com" target="_blank">Docker Desktop</a>

2. Для работы с системой контроля версий – |link_git|

.. |link_git| raw:: html

   <a href="https://github.com/git-guides/install-git" target="_blank">Git</a>

3. IDE для работы с исходным кодом – |link_pycharm|

.. |link_pycharm| raw:: html

    <a href="https://www.jetbrains.com/ru-ru/pycharm/download" target="_blank">PyCharm</a>


Установка
=========

Клонируйте репозиторий проекта в свою рабочую директорию:

.. code-block:: console

    git clone https://github.com/mnv/python-course-favorite-places.git

Перед началом использования приложения необходимо его сконфигурировать.

.. note::

    Для конфигурации выполните команды, описанные ниже, находясь в корневой директории проекта (на уровне с директорией `src`).

1. Скопируйте файл настроек `.env.sample`, создав файл `.env`:

    .. code-block:: console

        cp .env.sample .env

    Этот файл содержит преднастроенные переменные окружения, значения которых будут общими для всего приложения.
    Файл примера (`.env.sample`) содержит набор переменных со значениями по умолчанию.
    Созданный файл `.env` можно настроить в зависимости от окружения.

    .. warning::

        Никогда не добавляйте в систему контроля версий заполненный файл `.env` для предотвращения компрометации информации о конфигурации приложения.

2. Соберите Docker-контейнер с помощью Docker Compose:

    .. code-block:: console

     docker compose build

    Данную команду необходимо выполнять повторно в случае обновления зависимостей в файле `requirements.txt`.

3. После сборки контейнеров можно их запустить командой:

    .. code-block:: console

        docker compose up

   Когда запуск завершится, сервер начнет работать по адресу |link_url| (для Windows: |link_w|). 

.. |link_url| raw:: html

    <a href="http://0.0.0.0:8000/graphql" target="_blank">http://0.0.0.0:8000/graphql</a>

.. |link_w| raw:: html

    <a href="http://127.0.0.1:8000/graphql" target="_blank">http://127.0.0.1:8000/graphql</a>



Использование
=============

Запросы
-------

Пример запроса списка любимых мест:

.. code-block:: console

        query {
            places {
                latitude
                longitude
                description
                city
                locality
            }
        }

Пример запроса списка любимых мест с информацией о стране и новостях:

.. code-block:: console

    query {
        places {
            latitude
            longitude
            description
            city
            locality
            country {
                name
                capital
                alpha2code
                alpha3code
                capital
                region
                subregion
                population
                latitude
                longitude
                demonym
                area
                numericCode
                flag
                currencies
                languages
                news {
                    source {
                        id
                        name
                    }
                    author
                    title
                    description
                    url
                    urlToImage
                    publishedAt
                    content
                }
            }
        }
    }

Этот запрос оптимизироанно потребует дополнительную информацию про соответствующие страны и их новости, используя загрузчики данных для предотвращения проблемы N+1.

Пример зарпоса для получения определенного места:


.. code-block:: console

        query {
            place(id:1) {
                latitude
                longitude
                description
                city
                locality
            }
        }


Проект содержит специальный файл (`Makefile`) для автоматизации выполнения команд:

1. Сборка Docker-контейнера:

    .. code-block:: console

        make build

2. Генерация документации:

    .. code-block:: console

        make docs-html

3. Запуск форматирования кода:

    .. code-block:: console

        make format

4. Запуск статического анализа кода (выявление ошибок типов и форматирования кода):

    .. code-block:: console

        make lint

5. Запуск автоматических тестов:

    .. code-block:: console

        make test

    Покрытие тестов будет находиться в `src/htmlcov/index.html`.
    Чтобы вы могли оценить качество покрытия автоматических тестов.
    
Автоматизация
=============


Проект содержит специальный файл (`Makefile`) для автоматизации выполнения команд:

1. Сборка Docker-контейнера:

    .. code-block:: console

        make build

2. Генерация документации:

    .. code-block:: console

        make docs-html

3. Запуск форматирования кода:

    .. code-block:: console

        make format

4. Запуск статического анализа кода (выявление ошибок типов и форматирования кода):

    .. code-block:: console

        make lint

5. Запуск автоматических тестов:

    .. code-block:: console

        make test

    The test coverage report will be located at `src/htmlcov/index.html`.
    So you can estimate the quality of automated test coverage.

Документация 
============

Models
======

.. automodule:: models.countries
    :members:

.. automodule:: models.news
    :members:

.. automodule:: models.places
    :members:

Services
========

Countries 
---------

.. automodule:: services.countries
    :members:

News 
-------
.. automodule:: services.news
    :members:

Places 
-------
.. automodule:: services.places
    :members:

App 
=================

Context 
-------

.. automodule:: context
    :members:

Dataloaders
-----------

.. automodule:: dataloaders
    :members:

Schema
------

.. automodule:: schema
    :members:



