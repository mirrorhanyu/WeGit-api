import json
import os

from helpers.common.pagination import get_max_page
from helpers.decorators.require_requests_session import require_requests_session


@require_requests_session
def get_search(event, context, requests):
    github_api_host = os.environ.get('GITHUB_API_HOST')
    github_access_token = os.environ.get('GITHUB_ACCESS_TOKEN')
    search_headers = {
        'Authorization': f'token {github_access_token}'
    }
    search_parameters = {
        'q': event.get('queryStringParameters').get('repository'),
        'page': event.get('queryStringParameters').get('page')
    }
    search_url = f'{github_api_host}/search/repositories'
    search_response = requests.get(url=search_url, params=search_parameters, headers=search_headers)
    searches = search_response.json().get('items')
    headers = {'max-page': get_max_page(search_response.headers.get('Link'))}
    return {
        'statusCode': 200,
        'body': json.dumps(pick_from_search(searches)),
        'headers': headers
    }


def pick_from_search(searches):
    return [
        {
            'owner': search.get('owner').get('login'),
            'name': search.get('name'),
            'language': search.get('language'),
            'stargazersCount': search.get('stargazers_count'),
            'description': search.get('description'),
            'updatedAt': search.get('updated_at'),
        } for search in searches
    ]
