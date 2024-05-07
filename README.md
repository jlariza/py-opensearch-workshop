# Indexa tu información con OpenSearch y Python

OpenSearch es una herramienta poderosa y flexible para la indexación y gestión de datos. A su vez, Python es un lenguaje de programación popular y versátil que se puede utilizar para trabajar en gran cantidad de aplicaciones (Web, AI, Data Science, etc.)

En este taller aprenderás cómo integrar OpenSearch a un proyecto Python y así crear tu propio sistema de búsqueda con estas herramientas. Aprenderás a:

- Instalar y configurar OpenSearch 2.11.0 con docker
- Conectar OpenSearch a Python
- Indexar datos en OpenSearch
- Realizar búsquedas en OpenSearch
- Utilizar funcionalidades avanzadas de OpenSearch

¿Qué aprenderás?

- Qué es [OpenSearch](https://opensearch.org/) y qué es [opensearch-py](https://opensearch.org/docs/latest/clients/python-low-level/)
- Cómo crear tu propio sistema de búsqueda con OpenSearch y Django usando [django-opensearch-dsl](https://github.com/Codoc-os/django-opensearch-dsl)
- Cómo utilizar OpenSearch en un proyecto python que no use Django
- Cómo realizar búsquedas básicas e intermedias en tus datos

## Requisitos

En aras de facilitar el desarrollo del taller, solo requerirás tener instalado [docker](https://docs.docker.com/) y [docker-compose](https://docs.docker.com/compose/).

Si lo deseas, también puedes usar python directamente en tu máquina. En este caso, requerirás python 3.11 y un ambiente virtual. Te recomendamos usar [pyenv](https://github.com/pyenv/pyenv) y [virtualenv](https://virtualenv.pypa.io/en/latest/index.html).

> En caso de no usar docker, tendrás que instalar OpenSearch en tu máquina o en un servidor al que tengas acceso.

## Estructura del repositorio

En este repositorio encontrarás tres carpetas:

1. **opensearch-container**: Contiene el archivo `compose.yml` para configurar los contenedores de OpenSearch [^1]
2. **django_project**: Contiene un proyecto de ejemplo en Django, creado con [cookiecutter-django](https://github.com/cookiecutter/cookiecutter-django)
3. **pure python**: Contiene un script con ejemplos para usar opensearch-py

## Configuración de instancia local

1. ve a la carpeta **opensearch-container** y corre `docker compose up`. Luego, ve a [http://localhost:5601/](http://localhost:5601/). Una vez los nodos de OpenSearch hayan iniciado correctamente, verás el login del dashboard. Las credenciales por defecto son `admin / admin`.

> si lo deseas, puedes correr `docker compose up -d` para correr los contenedores de opensearch en un daemon.

2. ve a la carpeta **django_project** y corre

```
docker compose -f local.yml build
docker compose -f local.yml up
```

Luego, ve a [http://localhost:3000/](http://localhost:3000/). Verás la página de inicio por defecto de cookie cutter

> En caso de necesitar un usuario, puedes crearlo con `docker compose -f local.yml run --rm django python manage.py createsuperuser`. Sin embargo, no será requerido para el workshop.

### **django_project** - Pokemons y PokeAPI

En la parte Django de este workshop, crearemos una base de datos local de Pokemons que será indexada y consultada via OpenSearch.

Utilizaremos la información brindada por [PokeAPI](https://pokeapi.co/docs/v2) para generar información en nuestra base de datos.

Toda el código relacionado estará en la app [pokemons](django_project/opensearch_workshop/pokemons/)

Para cargar los datos, corre

```
docker compose -f local.yml run --rm django python manage.py loaddata pokemons
```

Esto creará los primeros 100 pokemons en tu base de datos.

> Si deseas crear más pokemons o agregar más datos a la base de datos, puedes consultar y modificar el script de consumo de la api [aquí](django_project/opensearch_workshop/pokemons/utils.py)

[^1]: [Install-opensearch/docker - opensearch.org](https://opensearch.org/docs/latest/install-and-configure/install-opensearch/docker/#sample-docker-composeyml)