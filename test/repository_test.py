import json
import os
import unittest

import requests_mock
from requests import HTTPError

import repository


class RepositoryTest(unittest.TestCase):
    os.environ['GITHUB_API_HOST'] = 'https://api.github.com'

    event = {
        'queryStringParameters': {
            'name': 'WeGit',
            'owner': 'mirrorhanyu'
        }
    }

    repository = {
        'id': 199455698,
        'node_id': 'MDEwOlJlcG9zaXRvcnkxOTk0NTU2OTg=',
        'name': 'WeGit',
        'full_name': 'mirrorhanyu/WeGit',
        'private': False,
        'owner': {
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
            'site_admin': False
        },
        'html_url': 'https://github.com/mirrorhanyu/WeGit',
        'description': 'unofficial github wechat mini program 民间 Github 微信小程序',
        'fork': False,
        'url': 'https://api.github.com/repos/mirrorhanyu/WeGit',
        'forks_url': 'https://api.github.com/repos/mirrorhanyu/WeGit/forks',
        'keys_url': 'https://api.github.com/repos/mirrorhanyu/WeGit/keys{/key_id}',
        'collaborators_url': 'https://api.github.com/repos/mirrorhanyu/WeGit/collaborators{/collaborator}',
        'teams_url': 'https://api.github.com/repos/mirrorhanyu/WeGit/teams',
        'hooks_url': 'https://api.github.com/repos/mirrorhanyu/WeGit/hooks',
        'issue_events_url': 'https://api.github.com/repos/mirrorhanyu/WeGit/issues/events{/number}',
        'events_url': 'https://api.github.com/repos/mirrorhanyu/WeGit/events',
        'assignees_url': 'https://api.github.com/repos/mirrorhanyu/WeGit/assignees{/user}',
        'branches_url': 'https://api.github.com/repos/mirrorhanyu/WeGit/branches{/branch}',
        'tags_url': 'https://api.github.com/repos/mirrorhanyu/WeGit/tags',
        'blobs_url': 'https://api.github.com/repos/mirrorhanyu/WeGit/git/blobs{/sha}',
        'git_tags_url': 'https://api.github.com/repos/mirrorhanyu/WeGit/git/tags{/sha}',
        'git_refs_url': 'https://api.github.com/repos/mirrorhanyu/WeGit/git/refs{/sha}',
        'trees_url': 'https://api.github.com/repos/mirrorhanyu/WeGit/git/trees{/sha}',
        'statuses_url': 'https://api.github.com/repos/mirrorhanyu/WeGit/statuses/{sha}',
        'languages_url': 'https://api.github.com/repos/mirrorhanyu/WeGit/languages',
        'stargazers_url': 'https://api.github.com/repos/mirrorhanyu/WeGit/stargazers',
        'contributors_url': 'https://api.github.com/repos/mirrorhanyu/WeGit/contributors',
        'subscribers_url': 'https://api.github.com/repos/mirrorhanyu/WeGit/subscribers',
        'subscription_url': 'https://api.github.com/repos/mirrorhanyu/WeGit/subscription',
        'commits_url': 'https://api.github.com/repos/mirrorhanyu/WeGit/commits{/sha}',
        'git_commits_url': 'https://api.github.com/repos/mirrorhanyu/WeGit/git/commits{/sha}',
        'comments_url': 'https://api.github.com/repos/mirrorhanyu/WeGit/comments{/number}',
        'issue_comment_url': 'https://api.github.com/repos/mirrorhanyu/WeGit/issues/comments{/number}',
        'contents_url': 'https://api.github.com/repos/mirrorhanyu/WeGit/contents/{+path}',
        'compare_url': 'https://api.github.com/repos/mirrorhanyu/WeGit/compare/{base}...{head}',
        'merges_url': 'https://api.github.com/repos/mirrorhanyu/WeGit/merges',
        'archive_url': 'https://api.github.com/repos/mirrorhanyu/WeGit/{archive_format}{/ref}',
        'downloads_url': 'https://api.github.com/repos/mirrorhanyu/WeGit/downloads',
        'issues_url': 'https://api.github.com/repos/mirrorhanyu/WeGit/issues{/number}',
        'pulls_url': 'https://api.github.com/repos/mirrorhanyu/WeGit/pulls{/number}',
        'milestones_url': 'https://api.github.com/repos/mirrorhanyu/WeGit/milestones{/number}',
        'notifications_url': 'https://api.github.com/repos/mirrorhanyu/WeGit/notifications{?since,all,participating}',
        'labels_url': 'https://api.github.com/repos/mirrorhanyu/WeGit/labels{/name}',
        'releases_url': 'https://api.github.com/repos/mirrorhanyu/WeGit/releases{/id}',
        'deployments_url': 'https://api.github.com/repos/mirrorhanyu/WeGit/deployments',
        'created_at': '2019-07-29T13:12:58Z',
        'updated_at': '2019-08-06T13:39:09Z',
        'pushed_at': '2019-08-06T06:04:51Z',
        'git_url': 'git://github.com/mirrorhanyu/WeGit.git',
        'ssh_url': 'git@github.com:mirrorhanyu/WeGit.git',
        'clone_url': 'https://github.com/mirrorhanyu/WeGit.git',
        'svn_url': 'https://github.com/mirrorhanyu/WeGit',
        'homepage': "",
        'size': 176,
        'stargazers_count': 1,
        'watchers_count': 1,
        'language': 'TypeScript',
        'has_issues': True,
        'has_projects': True,
        'has_downloads': True,
        'has_wiki': True,
        'has_pages': False,
        'forks_count': 1,
        'mirror_url': None,
        'archived': False,
        'disabled': False,
        'open_issues_count': 4,
        'license': None,
        'forks': 1,
        'open_issues': 4,
        'watchers': 1,
        'default_branch': 'master',
        'permissions': {
            'admin': True,
            'push': True,
            'pull': True
        },
        'allow_squash_merge': True,
        'allow_merge_commit': True,
        'allow_rebase_merge': True,
        'network_count': 1,
        'subscribers_count': 1
    }

    readme_response = {
        "name": "README.md",
        "path": "README.md",
        "sha": "0a211a8ebc945d6f8c88232d4aae545cec4a6ba9",
        "size": 572,
        "url": "https://api.github.com/repos/mirrorhanyu/WeGit/contents/README.md?ref=master",
        "html_url": "https://github.com/mirrorhanyu/WeGit/blob/master/README.md",
        "git_url": "https://api.github.com/repos/mirrorhanyu/WeGit/git/blobs/0a211a8ebc945d6f8c88232d4aae545cec4a6ba9",
        "download_url": "https://raw.githubusercontent.com/mirrorhanyu/WeGit/master/README.md",
        "type": "file",
        "content": "IyBXZUdpdArpnZ7lrpjmlrkgR2l0SHViIOW+ruS/oeWwj+eoi+W6jzxicj4K\nCiMjIOaJq+eggeS9k+mqjDxicj4KIVttaW5pLXByb2dyYW0tcXJjb2RlXSho\ndHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vbWlycm9yaGFueXUv\nbXktYXNzZXRzLXdhcmVob3VzZS9tYXN0ZXIvV2VHaXQvbWluaS1wcm9ncmFt\nLXFyY29kZS5qcGcpCgojIyB3aWtpClt3aWtpXShodHRwczovL2dpdGh1Yi5j\nb20vbWlycm9yaGFueXUvV2VHaXQvd2lraSkg6K6w6L295LqG5bCP56iL5bqP\n55qE5byA5Y+R6L+H56iL77yM5bm25Lya5oyB57ut5L+d5oyB5pu05paw77yM\n5qyi6L+O6L+H5p2l6K6o6K6644CCCgojIyBob3cgdG8gcGxheSB3aXRoIFdl\nR2l0CmBgYApnaXQgY2xvbmUgZ2l0QGdpdGh1Yi5jb206bWlycm9yaGFueXUv\nV2VHaXQuZ2l0CmNkIFdlR2l0Cnlhcm4KeWFybiBkZXY6d2VhcHAKYGBgCgoj\nIyB0YXNrIHdhbGxzClt0YXNrIHdhbGxzXShodHRwczovL2dpdGh1Yi5jb20v\nbWlycm9yaGFueXUvV2VHaXQvaXNzdWVzKSDljIXlkKvkuoYgdG8gZG8sIGlu\nIHByb2dyZXNzIOWSjCBkb25lIOeahCB0YXNrc+OAggo=\n",
        "encoding": "base64",
        "_links": {
            "self": "https://api.github.com/repos/mirrorhanyu/WeGit/contents/README.md?ref=master",
            "git": "https://api.github.com/repos/mirrorhanyu/WeGit/git/blobs/0a211a8ebc945d6f8c88232d4aae545cec4a6ba9",
            "html": "https://github.com/mirrorhanyu/WeGit/blob/master/README.md"
        }
    }

    readme = '### WeGit README'

    @requests_mock.Mocker()
    def test_should_throw_exception_when_requesting_github_repository_api_fails(self, request_mock):
        request_mock.get(url='https://api.github.com/repos/mirrorhanyu/WeGit',
                         reason='request repository fails',
                         status_code=500)
        with self.assertRaises(HTTPError) as context:
            repository.get_repository(self.event, None)
        self.assertEqual(context.exception.response.reason, 'request repository fails')

    @requests_mock.Mocker()
    def test_should_return_correct_response_when_requesting_github_trending_api_success(self, request_mock):
        request_mock.get(url='https://api.github.com/repos/mirrorhanyu/WeGit',
                         text=json.dumps(self.repository),
                         status_code=200)
        request_mock.get(url='https://api.github.com/repos/mirrorhanyu/WeGit/readme',
                         text=json.dumps(self.readme_response),
                         status_code=200)
        request_mock.get(url='https://raw.githubusercontent.com/mirrorhanyu/WeGit/master/README.md',
                         text=self.readme,
                         status_code=200)

        repository_response = repository.get_repository(self.event, None)

        repository_response_status_code = repository_response.get('statusCode')
        repository_response_body = json.loads(repository_response.get('body'))

        self.assertEqual(repository_response_status_code, 200)
        self.assertEqual(len(repository_response_body.keys()), 7)
        self.assertEqual(repository_response_body.get('description'), 'unofficial github wechat mini program 民间 Github 微信小程序')
        self.assertEqual(repository_response_body.get('subscribersCount'), 1)
        self.assertEqual(repository_response_body.get('stargazersCount'), 1)
        self.assertEqual(repository_response_body.get('forksCount'), 1)
        self.assertEqual(repository_response_body.get('license'), None)
        self.assertEqual(repository_response_body.get('openIssues'), 4)
        self.assertEqual(repository_response_body.get('readme'), '### WeGit README')
