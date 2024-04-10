import os
import requests
import yaml
from flask import Flask, render_template, request

app = Flask(__name__)

# GitHub repository information
REPO_OWNER = "your_username"
REPO_NAME = "your_repository"
YAML_FILE_PATH = "path/to/config.yaml"

# GitHub credentials
GITHUB_TOKEN = "your_github_token"

# Authenticate with GitHub
headers = {"Authorization": f"token {GITHUB_TOKEN}"}

def get_yaml_content():
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{YAML_FILE_PATH}"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    content = response.json()
    yaml_content = yaml.safe_load(base64.b64decode(content['content']))
    return yaml_content

def update_yaml_content(new_content):
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{YAML_FILE_PATH}"
    current_content = get_yaml_content()
    current_content.update(new_content)
    updated_content = yaml.dump(current_content)
    data = {
        "message": "Update YAML file",
        "content": base64.b64encode(updated_content.encode()).decode(),
        "sha": content['sha']
    }
    response = requests.put(url, headers=headers, json=data)
    response.raise_for_status()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    client = request.form['client']
    mode = request.form['mode']
    files = request.form['files']

    # Update the YAML file with the new values
    update_yaml_content({'client': client, 'mode': mode, 'files': files})

    return 'Configuration submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
