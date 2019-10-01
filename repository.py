import json
import os

from helpers.decorators.require_requests_session import require_requests_session


@require_requests_session
def get_repository(event, context, requests):
    name = event.get('queryStringParameters').get('name')
    owner = event.get('queryStringParameters').get('owner')
    github_api_host = os.environ.get('GITHUB_API_HOST')
    github_access_token = os.environ.get('GITHUB_ACCESS_TOKEN')
    repository_url = f'{github_api_host}/repos/{owner}/{name}'
    repository_readme_url = f'{github_api_host}/repos/{owner}/{name}/readme'
    repository_headers = {
        'Authorization': f'token {github_access_token}'
    }
    repository_response = requests.get(url=repository_url, headers=repository_headers)
    readme_url = requests.get(url=repository_readme_url, headers=repository_headers)
    readme = requests.get(url=readme_url.json().get('download_url'), headers=repository_headers)
    repository = pick_from_repository(repository_response.json())
    repository.update({
        'readme': readme.text
    })
    return {
        'statusCode': 200,
        'body': json.dumps(repository)
    }


def pick_from_repository(repository):
    return {
        'description': repository.get('description'),
        'subscribersCount': repository.get('subscribers_count'),
        'stargazersCount': repository.get('stargazers_count'),
        'forksCount': repository.get('forks_count'),
        'license': repository.get('license'),
        'openIssues': repository.get('open_issues_count'),
    }
