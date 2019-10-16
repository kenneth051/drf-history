# Standard Library
import threading
import copy


class RequestMiddleware(object):
    """Class for getting the current request"""

    _requestdata = {}

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self._requestdata["body_data"] = copy.copy(request.body.decode("utf-8"))
        self._requestdata[threading.current_thread()] = request
        response = self.get_response(request)

        self._requestdata.pop(threading.current_thread(), None)
        return response

    @classmethod
    def get_request_data(cls, default=None):
        """returns the current request or none if there is no request"""
        return (
            cls._requestdata.get("body_data", None),
            cls._requestdata.get(threading.current_thread(), default),
        )
