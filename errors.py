import functools
import requests


def error_handler(error_types = [Exception]):
    """Generic error handler."""
    def decorator(func):
        functools.wraps(func)

        def wrapper(self, *args, **kwargs):
            try:
                func(self, *args, **kwargs)
            except tuple(error_types) as err:
                print(f"Error: {err}")

        return wrapper
    return decorator




def request_error_handler(func):
    functools.wraps(func)

    def wrapper(self, *args, **kwargs):
        try:
            result = func(self, *args, **kwargs)
        except requests.exceptions.HTTPError as e:
            print("HTTP error occurred: %s" % e)
            result = None
        except requests.exceptions.ConnectionError as e:
            print("Error: Connection error occurred. Check your internet connection and try again.: %s" % e)
            result = None
        except requests.exceptions.Timeout as e:
            print("Request timed out: %s" % e)
            result = None
        except requests.exceptions.RequestException as e:
            print("An error occurred while making the request: %s" % e)
            result = None
        return result

    return wrapper
