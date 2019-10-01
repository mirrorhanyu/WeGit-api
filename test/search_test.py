import json
import os
import unittest

import requests_mock
from requests import HTTPError

import search


class SearchTest(unittest.TestCase):
    os.environ['GITHUB_API_HOST'] = 'https://api.github.com'

    event = {
        'queryStringParameters': {
            'repository': 'WeGit',
            'page': 1
        }
    }

    search = {
        'total_count': 1091,
        'incomplete_results': False,
        'items': [
            {
                'id': 177736533,
                'node_id': 'MDEwOlJlcG9zaXRvcnkxNzc3MzY1MzM=',
                'name': '996.ICU',
                'full_name': '996icu/996.ICU',
                'private': False,
                'owner': {
                    'login': '996icu',
                    'id': 48942249,
                    'node_id': 'MDQ6VXNlcjQ4OTQyMjQ5',
                    'avatar_url': 'https://avatars3.githubusercontent.com/u/48942249?v=4',
                    'gravatar_id': '',
                    'url': 'https://api.github.com/users/996icu',
                    'html_url': 'https://github.com/996icu',
                    'followers_url': 'https://api.github.com/users/996icu/followers',
                    'following_url': 'https://api.github.com/users/996icu/following{/other_user}',
                    'gists_url': 'https://api.github.com/users/996icu/gists{/gist_id}',
                    'starred_url': 'https://api.github.com/users/996icu/starred{/owner}{/repo}',
                    'subscriptions_url': 'https://api.github.com/users/996icu/subscriptions',
                    'organizations_url': 'https://api.github.com/users/996icu/orgs',
                    'repos_url': 'https://api.github.com/users/996icu/repos',
                    'events_url': 'https://api.github.com/users/996icu/events{/privacy}',
                    'received_events_url': 'https://api.github.com/users/996icu/received_events',
                    'type': 'User',
                    'site_admin': False
                },
                'html_url': 'https://github.com/996icu/996.ICU',
                'description': 'Repo for counting stars and contributing. Press F to pay respect to glorious developers.',
                'fork': False,
                'url': 'https://api.github.com/repos/996icu/996.ICU',
                'forks_url': 'https://api.github.com/repos/996icu/996.ICU/forks',
                'keys_url': 'https://api.github.com/repos/996icu/996.ICU/keys{/key_id}',
                'collaborators_url': 'https://api.github.com/repos/996icu/996.ICU/collaborators{/collaborator}',
                'teams_url': 'https://api.github.com/repos/996icu/996.ICU/teams',
                'hooks_url': 'https://api.github.com/repos/996icu/996.ICU/hooks',
                'issue_events_url': 'https://api.github.com/repos/996icu/996.ICU/issues/events{/number}',
                'events_url': 'https://api.github.com/repos/996icu/996.ICU/events',
                'assignees_url': 'https://api.github.com/repos/996icu/996.ICU/assignees{/user}',
                'branches_url': 'https://api.github.com/repos/996icu/996.ICU/branches{/branch}',
                'tags_url': 'https://api.github.com/repos/996icu/996.ICU/tags',
                'blobs_url': 'https://api.github.com/repos/996icu/996.ICU/git/blobs{/sha}',
                'git_tags_url': 'https://api.github.com/repos/996icu/996.ICU/git/tags{/sha}',
                'git_refs_url': 'https://api.github.com/repos/996icu/996.ICU/git/refs{/sha}',
                'trees_url': 'https://api.github.com/repos/996icu/996.ICU/git/trees{/sha}',
                'statuses_url': 'https://api.github.com/repos/996icu/996.ICU/statuses/{sha}',
                'languages_url': 'https://api.github.com/repos/996icu/996.ICU/languages',
                'stargazers_url': 'https://api.github.com/repos/996icu/996.ICU/stargazers',
                'contributors_url': 'https://api.github.com/repos/996icu/996.ICU/contributors',
                'subscribers_url': 'https://api.github.com/repos/996icu/996.ICU/subscribers',
                'subscription_url': 'https://api.github.com/repos/996icu/996.ICU/subscription',
                'commits_url': 'https://api.github.com/repos/996icu/996.ICU/commits{/sha}',
                'git_commits_url': 'https://api.github.com/repos/996icu/996.ICU/git/commits{/sha}',
                'comments_url': 'https://api.github.com/repos/996icu/996.ICU/comments{/number}',
                'issue_comment_url': 'https://api.github.com/repos/996icu/996.ICU/issues/comments{/number}',
                'contents_url': 'https://api.github.com/repos/996icu/996.ICU/contents/{+path}',
                'compare_url': 'https://api.github.com/repos/996icu/996.ICU/compare/{base}...{head}',
                'merges_url': 'https://api.github.com/repos/996icu/996.ICU/merges',
                'archive_url': 'https://api.github.com/repos/996icu/996.ICU/{archive_format}{/ref}',
                'downloads_url': 'https://api.github.com/repos/996icu/996.ICU/downloads',
                'issues_url': 'https://api.github.com/repos/996icu/996.ICU/issues{/number}',
                'pulls_url': 'https://api.github.com/repos/996icu/996.ICU/pulls{/number}',
                'milestones_url': 'https://api.github.com/repos/996icu/996.ICU/milestones{/number}',
                'notifications_url': 'https://api.github.com/repos/996icu/996.ICU/notifications{?since,all,participating}',
                'labels_url': 'https://api.github.com/repos/996icu/996.ICU/labels{/name}',
                'releases_url': 'https://api.github.com/repos/996icu/996.ICU/releases{/id}',
                'deployments_url': 'https://api.github.com/repos/996icu/996.ICU/deployments',
                'created_at': '2019-03-26T07:31:14Z',
                'updated_at': '2019-10-01T11:35:34Z',
                'pushed_at': '2019-09-30T02:54:46Z',
                'git_url': 'git://github.com/996icu/996.ICU.git',
                'ssh_url': 'git@github.com:996icu/996.ICU.git',
                'clone_url': 'https://github.com/996icu/996.ICU.git',
                'svn_url': 'https://github.com/996icu/996.ICU',
                'homepage': 'https://996.icu',
                'size': 183108,
                'stargazers_count': 247449,
                'watchers_count': 247449,
                'language': 'Rust',
                'has_issues': False,
                'has_projects': False,
                'has_downloads': True,
                'has_wiki': False,
                'has_pages': False,
                'forks_count': 21261,
                'mirror_url': None,
                'archived': False,
                'disabled': False,
                'open_issues_count': 16750,
                'license': {
                    'key': 'other',
                    'name': 'Other',
                    'spdx_id': 'NOASSERTION',
                    'url': None,
                    'node_id': 'MDc6TGljZW5zZTA='
                },
                'forks': 21261,
                'open_issues': 16750,
                'watchers': 247449,
                'default_branch': 'master',
                'permissions': {
                    'admin': False,
                    'push': False,
                    'pull': True
                },
                'score': 174.41379
            }
        ]
    }

    search_headers = {
        'Link': '<https://api.github.com/search/repositories?q=996&page=2>; rel="next", <https://api.github.com/search/repositories?q=996&page=34>; rel="last"'
    }

    @requests_mock.Mocker()
    def test_should_throw_exception_when_requesting_github_search_api_fails(self, request_mock):
        request_mock.get(url='https://api.github.com/search/repositories?q=WeGit&page=1',
                         reason='request search fails',
                         status_code=500)
        with self.assertRaises(HTTPError) as context:
            search.get_search(self.event, None)
        self.assertEqual(context.exception.response.reason, 'request search fails')

    @requests_mock.Mocker()
    def test_should_return_correct_response_when_requesting_github_search_api_success(self, request_mock):
        request_mock.get(url='https://api.github.com/search/repositories?q=WeGit&page=1',
                         text=json.dumps(self.search),
                         status_code=200,
                         headers=self.search_headers)
        search_response = search.get_search(self.event, None)

        search_response_status_code = search_response.get('statusCode')
        search_response_body = json.loads(search_response.get('body'))
        search_response_headers = search_response.get('headers')

        self.assertEqual(search_response_status_code, 200)

        self.assertEqual(search_response_headers.get('max-page'), 34)

        self.assertEqual(len(search_response_body), 1)
        self.assertEqual(len(search_response_body[0].keys()), 6)
        self.assertEqual(search_response_body[0].get('owner'), '996icu')
        self.assertEqual(search_response_body[0].get('name'), '996.ICU')
        self.assertEqual(search_response_body[0].get('language'), 'Rust')
        self.assertEqual(search_response_body[0].get('stargazersCount'), 247449)
        self.assertEqual(search_response_body[0].get('description'),
                         'Repo for counting stars and contributing. Press F to pay respect to glorious developers.')
        self.assertEqual(search_response_body[0].get('updatedAt'), '2019-10-01T11:35:34Z')
