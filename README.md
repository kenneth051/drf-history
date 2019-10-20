[![Build Status](https://travis-ci.org/kenneth051/django-track-actions.svg?branch=develop)](https://travis-ci.org/kenneth051/django-track-actions)

[![Coverage Status](https://coveralls.io/repos/github/kenneth051/django-track-actions/badge.svg?branch=develop)](https://coveralls.io/github/kenneth051/django-track-actions?branch=develop)


**DJANGO-TRACK-ACTIONS**
---------------------------------


Django-track-actions is a simple Django app to track actions performed in a django app

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "track_actions" to your INSTALLED_APPS setting like this::

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
