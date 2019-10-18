**DJANGO HISTORY**
An app to track actions performed in a django app

=====
django-track-actions
=====

Django_Actions_History is a simple Django app to track actions performed in a django app

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "Django_Actions_History" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'track_actions',
    ]

2. Add `track_actions.requestMiddleware.RequestMiddleware` in settings under middlewares

    MIDDLEWARE = [
        ... ,
        'track_actions.requestMiddleware.RequestMiddleware',
    ]


3. Run `python manage.py migrate track_actions` to create the History model.
