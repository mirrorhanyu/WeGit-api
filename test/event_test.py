import json
import os
import unittest

import requests_mock
from requests import HTTPError

import event


class EventTest(unittest.TestCase):
    os.environ['GITHUB_API_HOST'] = 'https://api.github.com'

    event = {
        'queryStringParameters': {
            'name': 'mirrorhanyu',
            'page': 1
        }
    }

    received_event = [
        {
            'id': '10533604500',
            'type': 'WatchEvent',
            'actor': {
                'id': 12322740,
                'login': 'fi3ework',
                'display_login': 'fi3ework',
                'gravatar_id': '''''',
                'url': 'https://api.github.com/users/fi3ework',
                'avatar_url': 'https://avatars.githubusercontent.com/u/12322740?'
            },
            'repo': {
                'id': 168468458,
                'name': 'unadlib/usm',
                'url': 'https://api.github.com/repos/unadlib/usm'
            },
            'payload': {
                'action': 'started'
            },
            'public': True,
            'created_at': '2019-10-01T13:22:49Z'
        }
    ]

    received_event_headers = {
        'Link': '<https://api.github.com/user/7698256/received_events?page=2>; rel="next", '
                '<https://api.github.com/user/7698256/received_events?page=9>; rel="last"'
    }

    @requests_mock.Mocker()
    def test_should_throw_exception_when_requesting_github_event_api_fails(self, request_mock):
        request_mock.get(url='https://api.github.com/users/mirrorhanyu/received_events?page=1',
                         reason='request event fails',
                         status_code=500)
        with self.assertRaises(HTTPError) as context:
            event.get_event(self.event, None)
        self.assertEqual(context.exception.response.reason, 'request event fails')

    @requests_mock.Mocker()
    def test_should_return_correct_response_when_requesting_github_event_api_success(self, request_mock):
        request_mock.get(url='https://api.github.com/users/mirrorhanyu/received_events?page=1',
                         text=json.dumps(self.received_event),
                         status_code=200,
                         headers=self.received_event_headers)
        event_response = event.get_event(self.event, None)

        event_response_status_code = event_response.get('statusCode')
        event_response_body = json.loads(event_response.get('body'))
        event_response_headers = event_response.get('headers')

        self.assertEqual(event_response_status_code, 200)
        self.assertEqual(event_response_headers.get('max-page'), 9)

        self.assertEqual(len(event_response_body), 1)
        self.assertEqual(len(event_response_body[0].keys()), 6)
        self.assertEqual(event_response_body[0].get('type'), 'starred')
        self.assertEqual(event_response_body[0].get('createdAt'), '2019-10-01T13:22:49Z')
        self.assertEqual(event_response_body[0].get('actorName'), 'fi3ework')
        self.assertEqual(event_response_body[0].get('actorNickname'), 'fi3ework')
        self.assertEqual(event_response_body[0].get('actorAvatar'), 'https://avatars.githubusercontent.com/u/12322740?')
        self.assertEqual(event_response_body[0].get('repo'), 'unadlib/usm')
