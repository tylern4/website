from flask import Flask, render_template
import requests
import os

app = Flask(__name__, template_folder='templates')


header = {"Authorization": f"token {os.getenv('GITHUB_OAUTH')}"}
github_info = "https://api.github.com/users/{}"
github_repo = "https://api.github.com/users/{}/repos"


@app.route('/', defaults={'user': 'tylern4'})
@app.route('/<user>')
def hello_name(user):
    info_resp = requests.get(github_info.format(user), headers=header)
    if info_resp.status_code != 200:
        return render_template('404.html', user=user, github_code=info_resp)
    repo_resp = requests.get(github_repo.format(user), headers=header)
    return render_template('hello.html', user=user, body=info_resp.json(), repos=repo_resp.json())


if __name__ == '__main__':
    app.run(debug=True)
