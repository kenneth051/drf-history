[![Build Status](https://travis-ci.org/kenneth051/django-track-actions.svg?branch=develop)](https://travis-ci.org/kenneth051/django-track-actions)  [![Coverage Status](https://coveralls.io/repos/github/kenneth051/django-track-actions/badge.svg?branch=develop)](https://coveralls.io/github/kenneth051/django-track-actions?branch=develop)   [![Maintainability](https://api.codeclimate.com/v1/badges/fc8a5a15c480d2ad117d/maintainability)](https://codeclimate.com/github/kenneth051/django-track-actions/maintainability)


**DJANGO-TRACK-ACTIONS**
---------------------------------


Django-track-actions is a simple Django app to track actions performed in a django app.
The actions being tracked are *POST*,  *DELETE*, *PUT* and *PATCH*

Data being captured is 
-----------------------
| Data | Description|
| --- | --- |
| User | The current loggedin user making the request|
| request data(body) | Data being sent (POST, PATCH and  PUT)|
| response data | response data after the request is complete |
| table_name | name of the model the request is affecting |
| instance_id | The id of the created, updated or deleted model instance |
| method | The request method i.e POST, DELETE, PUT or PATCH |
| |  |


Quick start
-------------

1. Add `track_actions` to your INSTALLED_APPS setting

        INSTALLED_APPS = [
            ...,
            'track_actions',
        ]


2. Add `track_actions.requestMiddleware.RequestMiddleware` in settings under middlewares

        MIDDLEWARE = [
            ... ,
            'track_actions.requestMiddleware.RequestMiddleware',
        ]


3. Run `python manage.py migrate track_actions` to create the History model.

You can create an endpoint to view all history from the History model by importing it in your view or serializers. 
        `from track_actions.models import History`

**NOTE**

This package will only work if you have a user in a request and a user model in your database.
