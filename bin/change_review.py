import requests
import json
import sys

github_access_token = '1e36286e38dc877f0919717c8952e7d19bc3ef9b'  # yasmamfk
domain = 'https://api.github.com'

headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'MFK-BOT'
}

def create_change_request_url(state, owner, repo, pr_num, token):
    url = domain + '/repos/{}/{}/pulls/{}/reviews?access_token={}'.format(owner, repo,
                                                                          pr_num,
                                                                          token)
    payload = {}
    payload['event'] = state
    payload['body'] = 'performed {} '.format(payload['event'])
    res = requests.post(url, data=json.dumps(payload), headers=headers)
    try:
        body = res.json()
        if not body:
            print('no response')
            return
        print(body)
        return body['id']
    except Exception as e:
        print(e)
