import sys
import requests


def create_pr_to_master(github_access_token):
    body = "## チェックリスト\n"
    # owner = 'mfkessai'
    owner = 'yasumamfk'
    repo = 'test_examination_model'
    branch_from = 'test-preview'
    branch_to = 'test-master'
    url = 'https://api.github.com/repos/{owner}/{repo}/pulls?access_token={token}'.format(owner,
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

    res = requests.post(url, headers, json=payload)
    print(res.content)


if __name__ == '__main__':
    # get file name from arg
    argvs = sys.argv
    token = argvs[2]
    create_pr_to_master(token)
