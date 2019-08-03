import requests


class ConnectionError(Exception):
    status_code = 503
    message = 'Github is unavailable'


class GithubFailureResponseError(Exception):

    def __init__(self, message, status_code):
        self.message = message
        self.status_code = status_code


def _do_request(path):
    URL_BASE = "https://api.github.com"

    url = URL_BASE + path
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        raise ConnectionError
    if not response.ok:
        raise GithubFailureResponseError(response.reason, response.status_code)
    return response.json()


def _get_filtered_response(keys, response):
    attrs = {}
    for k in keys:
        value = response.get(k, None)
        attrs[k] = "" if value is None else value
    return attrs


def get_user_profile(username):
    response_json = _do_request("/users/" + username)
    fields = ["id", "login", "name", "avatar_url", "html_url"]
    return _get_filtered_response(fields, response_json)


def get_user_repos(username):
    response_json = _do_request("/users/" + username + "/repos")
    fields = ["id", "name", "description", "html_url"]
    return [_get_filtered_response(
        fields, r) for r in response_json]
