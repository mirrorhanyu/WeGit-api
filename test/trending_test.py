import json
import os
import unittest

import requests_mock
from requests import HTTPError

import trending


class TrendingTest(unittest.TestCase):
    os.environ['GITHUB_TRENDING_HOST'] = 'https://github-trending-api.now.sh'

    event = {
        'queryStringParameters': {
            'since': 'weekly',
            'language': 'javascript'
        }
    }

    repositories = [
        {
            'author': 'qianguyihao',
            'name': 'Web',
            'avatar': 'https://github.com/qianguyihao.png',
            'url': 'https://github.com/qianguyihao/Web',
            'description': '前端入门和进阶学习笔记，超详细的Web前端学习图文教程。从零开始学前端，做一个Web全栈工程师。持续更新...',
            'language': 'JavaScript',
            'languageColor': '#f1e05a',
            'stars': 7188,
            'forks': 2008,
            'currentPeriodStars': 480,
            'builtBy': [
                {
                    'username': 'qianguyihao',
                    'href': 'https://github.com/qianguyihao',
                    'avatar': 'https://avatars1.githubusercontent.com/u/8827896'
                }
            ]
        }
    ]
    developers = [
        {
            'username': 'kmagiera',
            'name': 'Krzysztof Magiera',
            'type': 'user',
            'url': 'https://github.com/kmagiera',
            'avatar': 'https://avatars2.githubusercontent.com/u/726445',
            'repo': {
                'name': 'react-native-gesture-handler',
                'description': 'Declarative API exposing platform native touch and gesture system to React Native.',
                'url': 'https://github.com/kmagiera/react-native-gesture-handler'
            }
        }
    ]

    @requests_mock.Mocker()
    def test_should_throw_exception_when_requesting_github_trending_api_fails(self, request_mock):
        request_mock.get(url='https://github-trending-api.now.sh/repositories?language=javascript&since=weekly',
                         reason='request repositories fails',
                         status_code=500)
        with self.assertRaises(HTTPError) as context:
            trending.get_trending_repositories_and_developers(self.event, None)
        self.assertEqual(context.exception.response.reason, 'request repositories fails')

    @requests_mock.Mocker()
    def test_should_return_correct_response_when_requesting_github_trending_api_success(self, request_mock):
        request_mock.get(url='https://github-trending-api.now.sh/repositories?language=javascript&since=weekly',
                         text=json.dumps(self.repositories),
                         status_code=200)
        request_mock.get(url='https://github-trending-api.now.sh/developers?language=javascript&since=weekly',
                         text=json.dumps(self.developers),
                         status_code=200)

        trending_response = trending.get_trending_repositories_and_developers(self.event, None)

        trending_response_status_code = trending_response.get('statusCode')
        trending_response_body = json.loads(trending_response.get('body'))

        self.assertEqual(trending_response_status_code, 200)

        trending_repositories = trending_response_body.get('repositories')
        self.assertEqual(len(trending_repositories), 1)
        self.assertEqual(len(trending_repositories[0].keys()), 7)
        self.assertEqual(trending_repositories[0].get('author'), 'qianguyihao')
        self.assertEqual(trending_repositories[0].get('name'), 'Web')
        self.assertEqual(trending_repositories[0].get('description'),
                         '前端入门和进阶学习笔记，超详细的Web前端学习图文教程。从零开始学前端，做一个Web全栈工程师。持续更新...')
        self.assertEqual(trending_repositories[0].get('language'), 'JavaScript')
        self.assertEqual(trending_repositories[0].get('stars'), 7188)
        self.assertEqual(trending_repositories[0].get('forks'), 2008)
        self.assertEqual(trending_repositories[0].get('currentPeriodStars'), 480)

        trending_developers = trending_response_body.get('developers')
        self.assertEqual(len(trending_developers), 1)
        self.assertEqual(len(trending_developers[0].keys()), 4)
        self.assertEqual(trending_developers[0].get('username'), 'kmagiera')
        self.assertEqual(trending_developers[0].get('avatar'), 'https://avatars2.githubusercontent.com/u/726445')
        self.assertEqual(trending_developers[0].get('repoName'), 'react-native-gesture-handler')
        self.assertEqual(trending_developers[0].get('repoDescription'),
                         'Declarative API exposing platform native touch and gesture system to React Native.')
