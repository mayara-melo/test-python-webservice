import unittest
from github import GithubConsultant


class TestGithubConsultant(unittest.TestCase):
    def test_get_user_profile(self):
        """
        Test getting user profile
        """
        user_profiles = GithubConsultant.get_user_profile(
            username='mayara-melo')

        self.assertIsInstance(user_profiles, dict)

    def test_get_user_repos(self):
        """
        Test getting user repos
        """
        user_profiles = GithubConsultant.get_user_repos(
            username='mayara-melo')

        self.assertIsInstance(user_profiles, dict)


if __name__ == '__main__':
    unittest.main()
