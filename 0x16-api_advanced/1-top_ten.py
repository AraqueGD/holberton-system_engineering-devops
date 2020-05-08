#!/usr/bin/python3
""" 1. Top Ten """

import requests


def top_ten(subreddit):
    """
        Function Top ten recent post API REDDIT
    """
    url = ('https://www.reddit.com/r/{}/hot.json'.format(subreddit))
    user_agent = {'User-agent': 'My user-agent'}
    r_post = requests.get(url, headers=user_agent,
                          allow_redirects=False, params={'limit': 10})

    if (r_post.status_code == 200):
        r_json = r_post.json()
        list_post = r_json['data']['children']
        for post in range(len(list_post)):
            title = list_post[post]['data']['title']
            print(title)
    else:
        print('None')
