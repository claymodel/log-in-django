Log in Django
==============

Installation
============

.. code-block:: python

    pip install git+https://github.com/claymodel/log-in-django

or

.. code-block:: python

    pip install log-in-django

Quick start
===========
1. Add "django_logging" to your INSTALLED_APPS settings like this:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'log_in_django',
    )


2. Include the DjangoLoggingMiddleware middleware in your MIDDLEWARE_CLASSES like this:

.. code-block:: python

    MIDDLEWARE_CLASSES = (
        'log_in_django.middleware.DjangoLoggingMiddleware',
        ...
    )

Handlers
========

AppFileHandler
--------------

This handle will log request/response info to ``LOG_PATH/application.log``. It will also log request/exception, for unhandled exceptions, in the same file.
Log format:

Request and Response

.. code-block:: javascript

    {
        "INFO":
        {
            "timestamp":
            {
                "request": {
                ... request info ...
                },
                "response": {
                ... response info ...
                }
            }
        }
    }

Request and Exception

.. code-block:: javascript

    {
        "ERROR":
        {
            "timestamp":
            {
                "request": {
                ... request info ...
                },
                "exception": {
                    "message": "Exception message",
                    "traceback": [
                        ...
                    ]
                }
            }
        }
    }

SQLFileHandler
--------------

This handler will log all queries to ``LOG_PATH/sql.log``.
In a production environment you should set ``LOG_LEVEL = Error`` or ``SQL_LOG = False`` to avoid performance issues.
The queries will also be logged to the console if ``CONSOLE_LOG`` is set to ``True``

DebugFileHandler
----------------

This handler will log debug messages to ``LOG_PATH/debug.log``. This handler is only used when ``settings.DEBUG`` is set to ``True``.

Log format:

.. code-block:: python

    [%(levelname)s - %(created)s], file:%(module)s.py, func:%(funcName)s, ln:%(lineno)s: %(message)s


Custom Use
==========


To log debug messages:

.. code-block:: python

    from log_in_django import log

    log.debug('debug message')

To log handled exceptions:

.. code-block:: python

    from log_in_django import log, ErrorLogObject

    log.error(ErrorLogObject(request, exception, duration))


Settings
========
To override Django Logging settings, add a dictionary in your project's settings file

.. code-block:: python

    DJANGO_LOGGING = {
        "CONSOLE_LOG": False
    }

Default Settings
----------------

```CONSOLE_LOG = True``` - Log to console.

```SQL_LOG = True``` - Log SQL queries.

```SQL_THRESHOLD = 0.5``` - Log slow queries only.

```LOG_LEVEL = 'debug'``` - If settings.DEBUG is set to True, otherwise LOG_LEVEL is set to 'info'

```DISABLE_EXISTING_LOGGERS = True``` - Set this to False if you want to combine with multiple loggers.

```LOG_PATH = '{}/logs'.format(settings.BASE_DIR)``` - If the logs folder does not exist, it will be created.

```IGNORED_PATHS = ['/admin', '/static', '/favicon.ico']``` - List of URL endpoints to ignore.

```RESPONSE_FIELDS = ('status', 'reason', 'charset', 'headers', 'content')``` - List of response fields to log.

```CONTENT_JSON_ONLY = True``` - Log response content only if its a JSON document.

```ROTATE_MB = 100``` - Maximum size in MB that the log file can have before it gets rotated.

```ROTATE_COUNT = 10``` - Maximum number of rotated log files.

```INDENT_CONSOLE_LOG = 2``` - Indent console log by "n" spaces.

```ELASTICSEARCH_ENABLED = False``` - Set to yes to enable elasticsearch support.

```ELASTICSEARCH_HOSTS = ["localhost"]``` - Elasticsearch hosts

```ELASTICSEARCH_INDEX = "log-in-django-json"``` - Elasticsearch index name

```ELASTICSEARCH_SSL = False``` - Elasticsearch connection via SSL (:443)

```ELASTICSEARCH_AUTH = ('user', 'password)``` - Elasticsearch authorization credentials (user, password). Defaults to `None`

