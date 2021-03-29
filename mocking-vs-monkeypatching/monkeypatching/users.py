import requests
import json

def get_user_followers(username):
    """Grab the JSON object from a given user's followers."""
    response = requests.get('https://api.github.com/users/{}/followers'.format(username))
    return response.content

def get_follower_names(username):
    """Given a username of a GitHub user, return a list of follower usernames."""
    json_out = get_user_followers(username)
    as_dict = json.loads(json_out)
    return list(map(lambda x: x["login"], as_dict))