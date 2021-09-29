#!/usr/bin/python3
"""Module with top_ten function"""
import requests


def top_ten(subreddit):
    """ show the top 10 posts in a subreddit """
    try:
        # Change the user agent
        headers = {'User-Agent': 'Mozilla/5.0\
                    (Windows NT 10.0; Win64; x64)\
                    AppleWebKit/537.36 (KHTML, like Gecko)\
                    Chrome/93.0.4577.82 Safari/537.36'}
        payload = {'t': 'all', 'limit': '10'}
        request = requests.get('https://api.reddit.com/r/{}/'.
                               format(subreddit), headers=headers,
                               params=payload)
        top_posts = request.json()

        for post in top_posts['data']['children']:
            print(post['data']['title'])

    except Exception as ex:
        print("None")
