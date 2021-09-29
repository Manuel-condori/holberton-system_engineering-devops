#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Queries the Reddit API and returns a list of titles of hot articles"""
    after = str(after)
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json?after=" + after
    headers = {'User-Agent': 'Mozilla/5.0\
                (Windows NT 10.0; Win64; x64)\
                AppleWebKit/537.36 (KHTML, like Gecko)\
                Chrome/93.0.4577.82 Safari/537.36'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        posts = response.json()['data']['children']
        for title in posts:
            hot_list.append((title['data']['title']))
        after = response.json()['data']['after']
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list

    else:
        return None
