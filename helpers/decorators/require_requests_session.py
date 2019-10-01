import functools
import logging

import requests


def require_requests_session(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        requests_session = requests.Session()
        requests_session.hooks.update({
            'response': [log_request_and_response, raise_for_status]
        })
        return func(*args, **kwargs, requests=requests_session)

    return wrapper


def log_request_and_response(response, *args, **kwargs):
    log_request(response.request)
    log_response(response)


def raise_for_status(response, *args, **kwargs):
    response.raise_for_status()


def log_request(request):
    logging.info('request to: {}, method: {}, headers: {}, data: {}'.format(request.url, request.method,
                                                                            request.headers,
                                                                            request.body))


def log_response(response):
    logging.info('response from: {}, method: {}, headers: {}, data: {}'.format(response.request.url,
                                                                               response.request.method,
                                                                               response.headers,
                                                                               response.text))
