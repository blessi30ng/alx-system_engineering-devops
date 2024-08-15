#!/usr/bin/python3
"""
returns no of subs from reddit api
"""
import sys
import requests



def add_title(hot_list, hot_posts):
    """adds to list"""
    if len(hot_posts) == 0:
        return
    hot_list.append(hot_posts[0]['data']['title'])
    hot_posts.pop(0)
    add_title(hot_list, hot_posts)


def recurse(subreddit, hot_list=[], after=None):
    """queries redit api"""
    agent = 'Mozilla/5.0'
    headers = {
            'User-Agent': agent
    }


    params = {
            'after': after
    }

    req = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(req,
            headers=headers,
            params=params,
            allow_redirects=False)

    if res.status_code != 200:
        return None

    dict = res.json()
    hot_posts = dict['data']['children']
    add_title(hot_list, hot_posts)
    after = dict['data']['after']
    if not after:
        return hot_list
    return recurse(subreddit, hot_list=hot_list, after=after)
