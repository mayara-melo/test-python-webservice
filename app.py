from services.github import get_user_profile, get_user_repos, ConnectionError, GithubFailureResponseError
from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/users/<username>')
def get_users(username):
    user_profile = get_user_profile(username)
    return jsonify({
        'success': True,
        'result': user_profile
    }), 200


@app.route('/users/<username>/repos')
def get_users_repos(username):
    user_repos = get_user_repos(username)
    return jsonify({
        'success': "True",
        'result': user_repos
    }), 200


@app.errorhandler(Exception)
def handle_error(error):
    error_class = error.__class__
    # customized exception
    if(error_class == GithubFailureResponseError or error_class == ConnectionError):
        message = error.message
        status_code = error.status_code
        success = False
        response = {
            'success': success,
            'error': {
                'type': error.__class__.__name__,
                'message': message
            }
        }
        return jsonify(response), status_code
    # general
    else:
        return jsonify({
            'success': False,
            'error': error.description
        }), error.code
