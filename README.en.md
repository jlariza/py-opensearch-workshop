# Index your information with OpenSearch and Python

[![es](https://img.shields.io/badge/lang-es-red.svg)](/README.md) [![en](https://img.shields.io/badge/lang-en-blue.svg)](/README.en.md) [![GitHub License](https://img.shields.io/github/license/jlariza/py-opensearch-workshop)](/LICENSE)

OpenSearch is a powerful and flexible tool for indexing and data management. At the same time, Python is a popular and versatile programming language that can be used to work in many applications (Web, AI, Data Science, etc.).

In this workshop you will learn how to integrate OpenSearch into a Python project and thus create your own search system with these tools. You will learn how to:

- Install and configure OpenSearch 2.11.0 with docker.
- Connect OpenSearch to Python
- Index data in OpenSearch
- Perform OpenSearch searches
- Use advanced features of OpenSearch

What will you learn?

- What is [OpenSearch](https://opensearch.org/) and what is [opensearch-py](https://opensearch.org/docs/latest/clients/python-low-level/)
- How to create your own search system with OpenSearch and Django using [django-opensearch-dsl](https://github.com/Codoc-os/django-opensearch-dsl)
- How to use OpenSearch in a python project that does not use Django
- How to perform basic and intermediate searches on your data

## Requirements

In order to facilitate the development of the workshop, you only need to have [docker](https://docs.docker.com/) and [docker-compose](https://docs.docker.com/compose/) installed.

If you wish, you can also use python directly on your machine. In this case, you will need python 3.11 and a virtual environment. We recommend using [pyenv](https://github.com/pyenv/pyenv) and [virtualenv](https://virtualenv.pypa.io/en/latest/index.html).

> In case you do not use docker, you will have to install OpenSearch on your machine or on a server you have access to.

## Repository structure

In this repository you will find three folders:

1. **opensearch-container**: Contains the `compose.yml` file to configure the OpenSearch containers [^1]
2. **django_project**: Contains a Django example project, created with [cookiecutter-django](https://github.com/cookiecutter/cookiecutter-django)
3. **pure_python**: Contains a minimalistic [flask](https://flask.palletsprojects.com/en/3.0.x/) with examples for using opensearch-py.

## Local instance configuration

1. go to the **opensearch-container** folder and run `docker compose up`. Then, go to [http://localhost:5601/](http://localhost:5601/). Once the OpenSearch nodes have successfully started, you will see the dashboard login. The default credentials are `admin / admin`.

> You can run `docker compose up -d` to run the opensearch containers in a daemon if you wish.

2. go to the **django_project** folder and run

```bash
docker compose -f local.yml build
docker compose -f local.yml up
```

Then, go to [http://localhost:3000/](http://localhost:3000/). You will see the default cookie cutter home page.

> In case you need a user, you can create it with `docker compose -f local.yml run --rm django python manage.py createsuperuser`. However, it will not be required for the workshop.

3. go to the **pure_python** folder and run

```bash
docker compose build
docker compose up
```

Then go to [localhost:8000](http://localhost:8000/). You will see a `Hello World`.

## **django_project** - Pokemons and PokeAPI

In the Django part of this workshop, we will create a local database of Pokemons that will be indexed and queried via OpenSearch.

We will use the information provided by [PokeAPI](https://pokeapi.co/docs/v2) to generate information in our database.

All the related code will be in the [pokemons](django_project/opensearch_workshop/pokemons/) app.

To load the data, run

```bash
docker compose -f local.yml run --rm django python manage.py loaddata pokemons
```

This will create the first 100 pokemons in your database.

> If you want to create more pokemons or add more data to the database, you can refer to and modify the api consuming script [here](django_project/opensearch_workshop/pokemons/utils.py)

### **django_project** - [OpenSearch management commands](https://django-opensearch-dsl.readthedocs.io/en/latest/management/)

- To create your project's indexes in OpenSearch, run:

```bash
docker compose -f local.yml run --rm django python manage.py opensearch index create
```

> If you modify any index, you can recreate it with `docker compose -f local.yml run --rm django python manage.py opensearch index rebuild`.

- To index your database instances, run:

```bash
docker compose -f local.yml run --rm django python manage.py opensearch document index
```

## **pure_python**

In the pure python part of the workshop, we will query the OpenSearch pokemon index created with the Django app; this time using the [opensearch-py](https://opensearch.org/docs/latest/clients/python-low-level/) library. We will use a flask app to generate a simple interface.

Translated with [DeepL.com (free version)](https://www.deepl.com/)

[^1]: [Install-opensearch/docker - opensearch.org](https://opensearch.org/docs/latest/install-and-configure/install-opensearch/docker/#sample-docker-composeyml)
