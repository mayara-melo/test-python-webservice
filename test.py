import unittest
from github import GithubConsultant


class TestGithubConsultant(unittest.TestCase):
    def test_get_valid_user_profile(self):
        """
        Test getting user profile
        """
        user_profile = GithubConsultant.get_user_profile(
            username='mayara-melo')
        self.assertDictEqual(user_profile, {
            "id": 6036370,
            "login": "mayara-melo",
            "name": "",
            "avatar_url": "https://avatars3.githubusercontent.com/u/6036370?v=4",
            "html_url": "https://github.com/mayara-melo"
        })

    def test_get_valid_user_repos(self):
        """
        Test getting user repos
        """
        user_repos = GithubConsultant.get_user_repos(
            username='mayara-melo')

        self.assertCountEqual(user_repos, [
            {
                "id": 31819396,
                "name": "analise-juridica",
                "html_url": "https://github.com/mayara-melo/analise-juridica",
                "description": ""
            },
            {
                "id": 44837872,
                "name": "juridicNetworks",
                "html_url": "https://github.com/mayara-melo/juridicNetworks",
                "description": ""
            },
            {
                "id": 27124419,
                "name": "projeto_sbc",
                "html_url": "https://github.com/mayara-melo/projeto_sbc",
                "description": "Projeto da disciplina Sistemas Baseados em Conhecimento"
            },
            {
                "id": 199935279,
                "name": "test-python-webservice",
                "html_url": "https://github.com/mayara-melo/test-python-webservice",
                "description": ""
            }
        ])


if __name__ == '__main__':
    unittest.main()
