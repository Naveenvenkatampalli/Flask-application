import os
import requests
import yaml
import base64
from flask import Flask, render_template, request

app = Flask(__name__)

# GitHub repository information
REPO_OWNER = "Naveenvenkatampalli"
REPO_NAME = "Flask-application"
YAML_FILE_PATH = os.path.join(".github", "workflows", "config.yaml")

# GitHub credentials
GITHUB_TOKEN = "github_token"

# Authenticate with GitHub
headers = {"Authorization": f"token {GITHUB_TOKEN}"}

def get_yaml_content():
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{YAML_FILE_PATH}"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    content = response.json()
    yaml_content = yaml.safe_load(base64.b64decode(content['content']))
    return yaml_content



def get_yaml_content():
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{YAML_FILE_PATH}"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    content = response.json()
    
    # Decode YAML content and return along with SHA hash
    return {
        "content": yaml.safe_load(base64.b64decode(content['content'])),
        "sha": content['sha']
    }
# def update_yaml_content(new_content):
#     url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{YAML_FILE_PATH}"
#     current_content = get_yaml_content()
#     current_content.update(new_content)
#     updated_content = yaml.dump(current_content)
#     data = {
#         "message": "Update YAML file",
#         "content": base64.b64encode(updated_content.encode()).decode(),
#         "sha": current_content['sha']
#     }
#     response = requests.put(url, headers=headers, json=data)
#     response.raise_for_status()

def update_yaml_content(updated_variables):
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{YAML_FILE_PATH}"
    current_content = get_yaml_content()
    
    # Check if 'env' section exists, if not, create it
    if 'env' not in current_content:
        current_content['env'] = {}
    
    # Update environment variables under 'env' section
    env_section = current_content['env']
    for key, value in updated_variables.items():
        env_section[key] = value
    
    # Dump the content without changing the format
    updated_content = yaml.dump(current_content, default_flow_style=False)
    
    # Encode and prepare data for API call
    data = {
        "message": "Update YAML file",
        "content": base64.b64encode(updated_content.encode()).decode(),
        "sha": current_content['sha']
    }
    
    # Send the update request
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
    update_yaml_content({'BASE_URL': client, 'SANITY': mode, 'FILES': files})

    return 'Configuration submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
