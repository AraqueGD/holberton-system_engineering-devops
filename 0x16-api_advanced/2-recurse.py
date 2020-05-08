#!/usr/bin/python3
""" 2. Recurse it! """
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
        Function Recurse Reddit
    """
    url_hot = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, after)
    h = {'User-Agent': 'My User Agent'}
    req = requests.get(url_hot, headers=h, allow_redirects=False)

    if (req.status_code == 200):
        req_json = req.json()
        data_list = req_json['data']['children']
        for i in data_list:
            hot_list.append(i['data']['title'])
        after = req_json['data']['after']
        if (after is not None):
            recurse(subreddit, hot_list, after)
        else:
            return (hot_list)
    else:
        return (None)
    return (hot_list)
