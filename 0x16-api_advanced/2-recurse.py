#!/usr/bin/python3
""" 2. Recurse it! """
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
        Function Recurse Reddit
    """
    url = ('https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit, after))
    user_agent = {'User-gent': 'My user agent'}
    r_titles = requests.get(url, headers=user_agent, allow_redirects=False)

    if (r_titles.status_code == 200):
        r_json = r_titles.json()
        list_title = r_json['data']['children']
        for title in list_title:
            hot_list.append(title['data']['title'])
        after = r_json['data']['children']
        if (after is not None):
            recurse(subreddit, hot_list, after)
        else:
            return(hot_list)
    else:
        return (None)
    return (hot_list)
