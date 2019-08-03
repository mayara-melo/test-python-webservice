import unittest
from services.github import get_user_profile, get_user_repos

from unittest.mock import Mock, patch
# from unittest.mock import Mock, patch


class TestGithubService(unittest.TestCase):
    # @patch('services.github.get_user_profile.requests.get')

    def test_get_user_profile_when_github_response_is_ok(self):
        """
        Test getting user profile
        """
        data_to_return = {
            "id": 6036370,
            "login": "mayara-melo",
            "name": "",
            "avatar_url": "https://avatars3.githubusercontent.com/u/6036370?v=4",
            "html_url": "https://github.com/mayara-melo"
        }
        full_github_response = dict({
            "node_id": "MDQ6VXNlcjYwMzYzNzA=",
            "gravatar_id": "",
            "url": "https://api.github.com/users/mayara-melo",
            "followers_url": "https://api.github.com/users/mayara-melo/followers",
            "following_url": "https://api.github.com/users/mayara-melo/following{/other_user}",
            "gists_url": "https://api.github.com/users/mayara-melo/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/mayara-melo/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/mayara-melo/subscriptions",
            "organizations_url": "https://api.github.com/users/mayara-melo/orgs",
            "repos_url": "https://api.github.com/users/mayara-melo/repos",
            "events_url": "https://api.github.com/users/mayara-melo/events{/privacy}",
            "received_events_url": "https://api.github.com/users/mayara-melo/received_events",
            "type": "User",
            "public_repos": 4,
            "public_gists": 0,
            "followers": 5,
            "following": 0,
            "created_at": "2013-11-26T01:36:56Z",
            "updated_at": "2019-07-31T22:06:06Z"
        }, **data_to_return)

        with patch('services.github.requests.get') as mock_get:
            mock_get.return_value.ok = True
            mock_get.return_value = Mock(ok=True)
            mock_get.return_value.json.return_value = full_github_response

            user_profile = get_user_profile(
                username='mayara-melo')
            self.assertDictEqual(user_profile, data_to_return)

    def test_get_user_profile_when_github_response_is_not_ok(self):
        """
        Test getting user profile when github request fails
        """
        with patch('services.github.requests.get') as mock_get:
            mock_get.return_value.ok = False
            self.assertRaises(Exception, get_user_profile,
                              'mayara-melo')

    def test_get_valid_user_repos_when_github_response_ok(self):
        """
        Test getting user repos when github response is ok
        """
        with patch('services.github.requests.get') as mock_get:
            resumed_repos = [
                {
                    "id": 31819396,
                    "name": "analise-juridica",
                    "html_url": "https://github.com/mayara-melo/analise-juridica",
                    "description": ""
                }, {
                    "id": 199935279,
                    "name": "test-python-webservice",
                    "html_url": "https://github.com/mayara-melo/test-python-webservice",
                    "description": ""
                }
            ]
            full_data_repos = [
                {
                    "id": 31819396,
                    "name": "analise-juridica",
                    "html_url": "https://github.com/mayara-melo/analise-juridica",
                    "description": "",
                    "forks_url": "https://api.github.com/repos/mayara-melo/analise-juridica/forks",
                    "collaborators_url": "https://api.github.com/repos/mayara-melo/analise-juridica/collaborators{/collaborator}",
                    "teams_url": "https://api.github.com/repos/mayara-melo/analise-juridica/teams",
                }, {
                    "id": 199935279,
                    "name": "test-python-webservice",
                    "html_url": "https://github.com/mayara-melo/test-python-webservice",
                    "description": "",
                    "forks_url": "https://api.github.com/repos/mayara-melo/analise-juridica/forks",
                    "collaborators_url": "https://api.github.com/repos/mayara-melo/analise-juridica/collaborators{/collaborator}",
                    "teams_url": "https://api.github.com/repos/mayara-melo/analise-juridica/teams",
                }
            ]
            mock_get.return_value.ok = True
            mock_get.return_value = Mock(ok=True)
            mock_get.return_value.json.return_value = full_data_repos
            user_repos = get_user_repos(
                username='mayara-melo')
            self.assertCountEqual(user_repos, resumed_repos)

    def test_get_valid_user_repos_when_github_response_is_not_ok(self):
        """
        Test getting user repos when github request fails
        """
        with patch('services.github.requests.get') as mock_get:
            mock_get.return_value.ok = False
            self.assertRaises(Exception, get_user_repos, 'mayara-melo')


if __name__ == '__main__':
    unittest.main()
