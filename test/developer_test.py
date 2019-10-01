import json
import os
import unittest

import requests_mock
from requests import HTTPError

import developer


class DeveloperTest(unittest.TestCase):
    os.environ['GITHUB_API_HOST'] = 'https://api.github.com'

    event = {
        'queryStringParameters': {
            'name': 'mirrorhanyu'
        }
    }

    developer = {
        'login': 'mirrorhanyu',
        'id': 7698256,
        'node_id': 'MDQ6VXNlcjc2OTgyNTY=',
        'avatar_url': 'https://avatars3.githubusercontent.com/u/7698256?v=4',
        'gravatar_id': "",
        'url': 'https://api.github.com/users/mirrorhanyu',
        'html_url': 'https://github.com/mirrorhanyu',
        'followers_url': 'https://api.github.com/users/mirrorhanyu/followers',
        'following_url': 'https://api.github.com/users/mirrorhanyu/following{/other_user}',
        'gists_url': 'https://api.github.com/users/mirrorhanyu/gists{/gist_id}',
        'starred_url': 'https://api.github.com/users/mirrorhanyu/starred{/owner}{/repo}',
        'subscriptions_url': 'https://api.github.com/users/mirrorhanyu/subscriptions',
        'organizations_url': 'https://api.github.com/users/mirrorhanyu/orgs',
        'repos_url': 'https://api.github.com/users/mirrorhanyu/repos',
        'events_url': 'https://api.github.com/users/mirrorhanyu/events{/privacy}',
        'received_events_url': 'https://api.github.com/users/mirrorhanyu/received_events',
        'type': 'User',
        'site_admin': False,
        'name': 'han',
        'company': '@thoughtworks',
        'blog': 'mirrorhanyu.com',
        'location': 'wuhan',
        'email': 'mirrorhanyu@gmail.com',
        'hireable': True,
        'bio': 'Hello, Im Han',
        'public_repos': 11,
        'public_gists': 0,
        'followers': 6,
        'following': 59,
        'created_at': '2014-05-26T02:46:44Z',
        'updated_at': '2019-04-25T01:45:33Z',
        'private_gists': 0,
        'total_private_repos': 0,
        'owned_private_repos': 0,
        'disk_usage': 51602,
        'collaborators': 0,
        'two_factor_authentication': False,
        'plan': {
            'name': 'free',
            'space': 976562499,
            'collaborators': 0,
            'private_repos': 10000
        }
    }

    @requests_mock.Mocker()
    def test_should_throw_exception_when_requesting_github_developer_api_fails(self, request_mock):
        request_mock.get(url='https://api.github.com/users/mirrorhanyu',
                         reason='request developer fails',
                         status_code=500)
        with self.assertRaises(HTTPError) as context:
            developer.get_developer(self.event, None)
        self.assertEqual(context.exception.response.reason, 'request developer fails')

    @requests_mock.Mocker()
    def test_should_return_correct_response_when_requesting_github_trending_api_success(self, request_mock):
        request_mock.get(url='https://api.github.com/users/mirrorhanyu',
                         text=json.dumps(self.developer),
                         status_code=200)
        developer_response = developer.get_developer(self.event, None)

        developer_response_status_code = developer_response.get('statusCode')
        developer_response_body = json.loads(developer_response.get('body'))

        self.assertEqual(developer_response_status_code, 200)
        self.assertEqual(len(developer_response_body.keys()), 11)
        self.assertEqual(developer_response_body.get('avatar'), 'https://avatars3.githubusercontent.com/u/7698256?v=4')
        self.assertEqual(developer_response_body.get('name'), 'han')
        self.assertEqual(developer_response_body.get('nickname'), 'mirrorhanyu')
        self.assertEqual(developer_response_body.get('bio'), 'Hello, Im Han')
        self.assertEqual(developer_response_body.get('repos'), 11)
        self.assertEqual(developer_response_body.get('followers'), 6)
        self.assertEqual(developer_response_body.get('following'), 59)
        self.assertEqual(developer_response_body.get('email'), 'mirrorhanyu@gmail.com')
        self.assertEqual(developer_response_body.get('blog'), 'mirrorhanyu.com')
        self.assertEqual(developer_response_body.get('company'), '@thoughtworks')
        self.assertEqual(developer_response_body.get('location'), 'wuhan')
