import json
import os

import requests


def get_trending_repositories_and_developers(event, context):
    since = event.get('queryStringParameters').get('since')
    language = event.get('queryStringParameters').get('language')
    github_trending_host = os.environ.get('GITHUB_TRENDING_HOST')
    trending_repositories_response = requests.get(
        f'{github_trending_host}/repositories?language={language}&since={since}')
    trending_developers_response = requests.get(f'{github_trending_host}/developers?language={language}&since={since}')
    trending_repositories_response.raise_for_status()
    trending_developers_response.raise_for_status()
    return {
        "statusCode": 200,
        "body": json.dumps({
            "repositories": trending_repositories_response.json(),
            "developers": trending_developers_response.json()
        })
    }
