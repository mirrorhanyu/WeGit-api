import json
import os

from helpers.common.pagination import get_max_page
from helpers.decorators.require_requests_session import require_requests_session


@require_requests_session
def get_event(event, context, requests):
    name = event.get('queryStringParameters').get('name')
    page = event.get('queryStringParameters').get('page')
    github_api_host = os.environ.get('GITHUB_API_HOST')
    github_access_token = os.environ.get('GITHUB_ACCESS_TOKEN')
    event_url = f'{github_api_host}/users/{name}/received_events'
    event_headers = {
        'Authorization': f'token {github_access_token}'
    }
    event_parameters = {
        'page': page
    }
    events_response = requests.get(url=event_url, params=event_parameters, headers=event_headers)
    headers = {'max-page': get_max_page(events_response.headers.get('Link'))}
    return {
        'statusCode': 200,
        'body': json.dumps(pick_from_event(events_response.json())),
        'headers': headers
    }


def pick_from_event(events):
    return [
        {
            'type': map_action_type(event.get('type')),
            'createdAt': event.get('created_at'),
            'actorName': event.get('actor').get('display_login'),
            'actorNickname': event.get('actor').get('login'),
            'actorAvatar': event.get('actor').get('avatar_url'),
            'repo': event.get('repo').get('name'),
        } for event in events
    ]


def map_action_type(type):
    mapping = {
        'WatchEvent': 'starred',
        'ForkEvent': 'forked',
        'CreateEvent': 'created a repository',
        'PublicEvent': 'made public on',
        'PushEvent': 'pushed to'
    }
    return mapping.get(type, f'{type.replace("Event", "").lower()}ed')
