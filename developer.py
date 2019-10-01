import json
import os

from helpers.decorators.require_requests_session import require_requests_session


@require_requests_session
def get_developer(event, context, requests):
    name = event.get('queryStringParameters').get('name')
    token = event.get('queryStringParameters').get('token')
    github_api_host = os.environ.get('GITHUB_API_HOST')
    github_access_token = os.environ.get('GITHUB_ACCESS_TOKEN')
    developer_url = f'{github_api_host}/user' if token is not None else f'{github_api_host}/users/{name}'
    developer_headers = {
        'Authorization': f'token {github_access_token}'
    }
    developer = requests.get(url=developer_url, headers=developer_headers)
    return {
        'statusCode': 200,
        'body': json.dumps(pick_from_developer(developer.json()))
    }


def pick_from_developer(developer):
    return {
        'avatar': developer.get('avatar_url'),
        'name': developer.get('name'),
        'nickname': developer.get('login'),
        'bio': developer.get('bio'),
        'repos': developer.get('public_repos'),
        'followers': developer.get('followers'),
        'following': developer.get('following'),
        'email': developer.get('email'),
        'blog': developer.get('blog'),
        'company': developer.get('company'),
        'location': developer.get('location')
    }
