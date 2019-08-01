#!/usr/bin/env python3
import requests


class GithubConsultant:
    URL_BASE = "api.github.com/users/"
    # headers = {"Accept": "application/vnd.github.v3+json"}
    # def __init__(self):
    #     self.host = 'github.com'

    @staticmethod
    def _get_filtered_response(keys, response):
        attrs = {}
        for k in keys:
            value = response.get(k, None)
            attrs[k] = "" if value is None else value
        return attrs

    @staticmethod
    def get_user_profile(username):
        url = f'https://api.github.com/users/{username}'
        response = requests.get(url)
        fields = ["id", "login", "name", "avatar_url", "html_url"]
        if response.status_code == 200:
            return GithubConsultant._get_filtered_response(fields, response.json())
        else:
            return 1

    @staticmethod
    def get_user_repos(username):
        url = f'https://api.github.com/users/{username}/repos'
        response = requests.get(url)
        if response.status_code == 200:
            fields = [
                "id",
                "name",
                "description",
                "html_url"
            ]
            repos = response.json()
            return [GithubConsultant._get_filtered_response(
                fields, r) for r in repos]
        else:
            return
