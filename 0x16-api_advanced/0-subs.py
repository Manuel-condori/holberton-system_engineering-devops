#!/usr/bin/python3
"""Find the number of subs"""
import requests


def number_of_subscribers(subreddit):
    ''' get number of reddit subcribers'''

    url = 'http://reddit.com/r/{}/about.json'
    headers = {'User-agent': 'Mozilla/5.0\
                (Windows NT 10.0; Win64; x64)\
                AppleWebKit/537.36\
                (KHTML, like Gecko)\
                Chrome/93.0.4577.82 Safari/537.36'}
    response = requests.get(url.format(subreddit), headers=headers)
    if response.status_code == 200:
        subs = response.json()
        '''subs0 = subs['data']['subscribers']'''
        subs0 = subs.get('data').get('subscribers')
        return subs0
    else:
        return 0
