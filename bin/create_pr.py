#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import requests
import json


def create_pr_to_master(owner, repo, github_access_token):
    body = "## チェックリスト\n"
    branch_from = 'yasumamfk:test-preview'
    branch_to = 'test-master'
    url = 'https://api.github.com/repos/{}/{}/pulls?access_token={}'.format(owner,
                                                                            repo,
                                                                            github_access_token)
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'MFK-BOT'
    }

    payload = {
        'title': "Set Default",
        'body': body,
        'head': branch_from,
        'base': branch_to
    }

    res = requests.post(url, data=json.dumps(payload), headers=headers)
    body = res.json()

    print(
        body['id'],
        body['number'],
        body['state'],
        body['title'],
        body['body'],
    )


if __name__ == '__main__':
    argvs = sys.argv
    github_access_token = argvs[1]
    create_pr_to_master(github_access_token)
