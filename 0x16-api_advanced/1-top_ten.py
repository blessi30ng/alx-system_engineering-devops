#!/usr/bin/python3
"""top ten hot posts of a subreddit"""

import sys
import requests


def top_ten(subreddit):
    """ top ten"""
    agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': agent
    }

    params = {
        'limit': 10
    }

    req =  "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(req,
            headers=headers,
            params=params,
            allow_redirects=False)
    if res.status_code != 200:
        print(None)
        return
    dict = res.json()
    hot_posts = dict['data']['children']
    if len(hot_posts) is 0:
        print(None)
    else:
        for post in hot_posts:
            print(post['data']['title'])
