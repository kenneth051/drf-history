**DJANGO HISTORY**
An app to track actions performed in a django app

=====
Django_Actions_History
=====

Django_Actions_History is a simple Django app to track actions performed in a django app

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "Django_Actions_History" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'Django_Actions_History',
    ]

2. Add `django_actions_history.requestMiddleware.RequestMiddleware` in settings under middlewares

    MIDDLEWARE = [
        ... ,
        'django_actions_history.requestMiddleware.RequestMiddleware',
    ]


3. Run `python manage.py migrate` to create the History models.
