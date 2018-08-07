
const app = {}
const pr = {}
const owner = 'mfkessai'
const branchFrom = 'mfkessai'
pr.url = `https://api.github.com/repos/${owner}/${branchFrom}/pulls?access_token=`
pr.body = "## チェックリスト\n"

function create_pr_to_master(pr,github_access_token) {

    const options = {
        method: 'POST',
        uri: pr.url + github_access_token,
        headers: {
            'Content-Type': 'application/json',
            'User-Agent': 'MFK-BOT'
        },
        body: {
            title: "Set Default",
            body: pr.body,
            head: "preview",
            base: "master"
        },
        json: true
    }

    request(options, function(error, response, body){
        if (!error && response.statusCode == 200) {
            console.log(body)
        } else {
            console.log('error: '+ response.statusCode + '\n' + response.body)
        }
    })
}