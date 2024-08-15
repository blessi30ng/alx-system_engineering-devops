#!/usr/bin/python3
"""no of subs for a given subreddit"""
import sys
import requests


def number_of_subscribers(subreddit):
    """queries reddit api"""
    agent = 'Mozilla/5.0'

    headers = {
            'User-Agent': agent
    }

    req = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(req, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return 0
    dict = res.json()
    if 'data' not in dict:
        return 0
    if 'subscribers' not in dict.get('data'):
        return 0
    return res.json()['data']['subscribers']
