#!/usr/bin/env python
# -*- coding: utf-8 -*-

# githubのmasterブランチにマージされた後で実行され、Githubのreleaseとtagを作成
# githubのrelease versionと、tag名は引数に渡された値を使用

import os
import sys
import requests
import json

# get file name from arg
argvs = sys.argv
argc = len(argvs)

#mfkessai
user = 'mfkessai'
repo = 'examination_model'
branch = 'preview'
host = 'api.github.com'
token = argvs[2]

headers = {
    'Authorization': 'token %s' % token,
    'Content-Type': 'application/json',
    'User-Agent': 'issue-hub release'
}


# create new release
def create_release(tag_version):
    print('create_release and tag')
    path = 'https://' + host + '/repos/%s/%s/releases' % (user, repo)
    params = {
        'tag_name': '%s' % tag_version,
        'target_commitish': branch,
        'name': 'v%s' % tag_version,
        'prerelease': False
    }
    resp = requests.post(path, data=json.dumps(params), headers=headers)
    result = json.loads(resp.content)

    is_error = result.get('errors', None)

    if is_error:
        print(is_error)
        return
    try:
        print(result['id'])
        print(result['upload_url'])
    except Exception as e:
        print(e)


if __name__ == '__main__':
    create_release(argvs[1])
