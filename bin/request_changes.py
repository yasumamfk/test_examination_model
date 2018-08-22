#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import requests
import json
from operator import itemgetter
from bin.utils.utils import read_config

config = read_config()
owner = config['owner']
repo = config['repo']
domain = config['domain']
headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'MFK-BOT'
}


def get_target_pr_number(token, owner, repo):
    f = 0
    url = domain + '/repos/{}/{}/pulls'.format(owner, repo)
    params = {
        'state': 'all',
        'sort': 'updated',
        'direction': 'desc',
        'access_token': token
    }
    res = requests.get(url, params=params)

    # Wait until PullRequest has successfully been thrown
    while f == 0:
        for i, r in enumerate(res.json()):
            if r['head']['ref'] == 'release' and r['base']['ref'] == 'master':
                return res.json()[i]['number']
        time.sleep(10)


def get_reviews(owner, repo, pr_num, token):
    """
    :param owner:
    :param repo:
    :param pr_num:
    :param token:
    :return: reviews: List
    """
    url = domain + '/repos/{}/{}/pulls/{}/reviews?access_token={}'.format(owner, repo, pr_num, token)
    res = requests.get(url, headers=headers)
    if not res.content:
        return
    return res.json()


def get_latest_action(reviews):
    """
    :param reviews: List
    :return: state: String
    """
    return sorted(reviews, key=itemgetter('submitted_at'), reverse=True)[0]['state']


def dispatch_event(state, evaluation):
    """
    dispatch event name depending on state
    :param state: String
    :param evaluation: Bool
    :return: event: String:
    """
    print(state, evaluation)
    if evaluation:
        return 'APPROVE'
    return 'REQUEST_CHANGES'


def push_change_request(event, comment, owner, repo, pr_num, token):
    url = domain + '/repos/{}/{}/pulls/{}/reviews?access_token={}'.format(owner, repo, pr_num, token)
    payload = {
        'event': event,
        'body': comment
    }
    res = requests.post(url, data=json.dumps(payload), headers=headers)
    try:
        body = res.json()
        if not body:
            print('NO RESPONSE')
            return
        return body['id']
    except Exception as e:
        print(e)


if __name__ == '__main__':
    argvs = sys.argv
    github_access_token = argvs[1]
    comment = argvs[2]
    evaluation = True if argvs[3] == 't' else False

    pr_num = get_target_pr_number(github_access_token, owner, repo)
    reviews = get_reviews(owner, repo, pr_num, github_access_token)

    if not reviews:
        push_change_request('COMMENT', owner, repo, pr_num, github_access_token)
    else:
        state = get_latest_action(reviews)
        event = dispatch_event(state, evaluation)
        # create_change_request_url(event, comment, owner, repo, pr_num, github_access_token)
