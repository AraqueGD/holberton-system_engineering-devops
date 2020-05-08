#!/usr/bin/python3
""" 1. How many Subs? """
import requests


def number_of_subscribers(subreddit):
    """
        Function count subscribers the API REDDIT
    """
    url = ('https://www.reddit.com/r/{}/about.json'.format(subreddit))
    user_agent = {'User-Agent': 'My User Agent'}
    r_sub = requests.get(url, headers=user_agent, allow_redirects=False)

    if (r_sub.status_code == 200):
        r_json = r_sub.json()
        count = r_json['data']['subscribers']
        return (count)
    return (0)
