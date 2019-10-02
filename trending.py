import json
import os

from helpers.decorators.require_requests_session import require_requests_session


@require_requests_session
def get_trending_repositories_and_developers(event, context, requests):
    github_trending_host = os.environ.get('GITHUB_TRENDING_HOST')
    trending_parameters = {
        'since': event.get('queryStringParameters').get('since'),
        'language': event.get('queryStringParameters').get('language')
    }
    trending_repositories_url = f'{github_trending_host}/repositories'
    trending_developers_url = f'{github_trending_host}/developers'
    trending_repositories_response = requests.get(url=trending_repositories_url, params=trending_parameters)
    trending_developers_response = requests.get(url=trending_developers_url, params=trending_parameters)
    return {
        'statusCode': 200,
        'body': json.dumps({
            'repositories': pick_from_repositories(trending_repositories_response.json()),
            'developers': pick_from_developers(trending_developers_response.json())
        })
    }


def pick_from_repositories(repositories):
    return [
        {
            'author': repository.get('author'),
            'name': repository.get('name'),
            'description': repository.get('description'),
            'language': repository.get('language'),
            'stars': repository.get('stars'),
            'forks': repository.get('forks'),
            'currentPeriodStars': repository.get('currentPeriodStars')
        } for repository in repositories
    ]


def pick_from_developers(developers):
    return [
        {
            'username': developer.get('username'),
            'avatar': developer.get('avatar'),
            'repoName': developer.get('repo').get('name'),
            'repoDescription': developer.get('repo').get('description')
        } for developer in developers
    ]
