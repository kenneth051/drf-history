[![Build Status](https://travis-ci.org/kenneth051/drf-history.svg?branch=develop)](https://travis-ci.org/kenneth051/drf-history)  [![Coverage Status](https://coveralls.io/repos/github/kenneth051/django-track-actions/badge.svg?branch=develop)](https://coveralls.io/github/kenneth051/django-track-actions?branch=develop)   [![Maintainability](https://api.codeclimate.com/v1/badges/fc8a5a15c480d2ad117d/maintainability)](https://codeclimate.com/github/kenneth051/django-track-actions/maintainability)  [![Downloads](https://pepy.tech/badge/drf-history)](https://pepy.tech/project/drf-history)   [![Downloads](https://pepy.tech/badge/drf-history/month)](https://pepy.tech/project/drf-history/month)  [![Downloads](https://pepy.tech/badge/drf-history/week)](https://pepy.tech/project/drf-history/week) 


**DRF-HISTORY**
---------------------------------


drf-history is a simple django rest framework app to track actions performed in a django app and to also gets the current request.
The actions being tracked are **POST**,  **DELETE**, **PUT** and **PATCH**

Data being captured is 
-----------------------
| Data | Description|
| --- | --- |
| user | The current loggedin user making the request|
| request data(body) | Data being sent (POST, PATCH and  PUT)|
| response data | response data after the request is complete |
| table_name | name of the model the request is affecting |
| instance_id | The id of the created, updated or deleted model instance |
| method | The request method i.e POST, DELETE, PUT or PATCH |
| created_at | Date time object for when the request is being carried out |
| path | path the request is coming from |
| | |


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

        `python manage.py migrate track_actions`
        

After this every POST, UPDATE and DELETE action will be recorded in your database under the history model.


**To get the current request**

To get the current request in progress anywhere in the application.

1. Import the relevant class.

        from track_actions.requestMiddleware import RequestMiddleware


2   Get the current request object.
                                
        current_request = RequestMiddleware.get_request_data()[1]


**To access the get history endpoint**

1. In your project's url file


        `import track_actions` 

2. Register the url in the urlpattern 

        `path('track_actions/', include('track_actions.urls'))`

3. visit the url in the browser or on postman

        `http://127.0.0.1:8000/track_actions/history/`
        
you should be able to see all the recorded history if you have `admin` priveleges and you are authenticated.


**Alternatively**

You can create your own endpoint to view all history from the History model by importing it in your views or serializers.

        `from track_actions.models import History`


**NOTE**

This package will only work if you have a user in a request and a user model in your database.
