import os
import requests
import yaml
import base64
from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

# GitHub repository information
REPO_OWNER = "Naveenvenkatampalli"
REPO_NAME = "Flask-application"
YAML_FILE_PATH = os.path.join(".github", "workflows", "config.yaml")

# GitHub credentials
GITHUB_TOKEN = "github_token"

# Authenticate with GitHub
headers = {"Authorization": f"token {GITHUB_TOKEN}"}

# def get_yaml_content():
#     url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{YAML_FILE_PATH}"
#     response = requests.get(url, headers=headers)
#     response.raise_for_status()
#     content = response.json()
#     yaml_content = yaml.safe_load(base64.b64decode(content['content']))
#     return yaml_content


def update_yaml_content(updated_variables):
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{YAML_FILE_PATH}"
    current_content, sha_hash = get_yaml_content()
    
    # Navigate to the specific job and step to update the 'env' section
    steps = current_content.get('jobs', {}).get('test', {}).get('steps', [])
    for step in steps:
        if step.get('name') == 'Run Selenium tests with Firefox':
            if 'env' not in step:
                step['env'] = {}
            step['env'].update(updated_variables)
            break  # Assuming only one step needs updating and then exit the loop
    
    # Dump the updated content to YAML
    updated_yaml = yaml.dump(current_content, Dumper=yaml.SafeDumper, default_flow_style=False, sort_keys=False)
    # print("this is updated_yaml", updated_yaml)
    
    # Encode content in base64 for GitHub API
    encoded_content = base64.b64encode(updated_yaml.encode()).decode()
    
    # Prepare data for API call
    data = {
        "message": "Update YAML file",
        "content": encoded_content,
        "sha": sha_hash
    }
    
    # Send the update request
    response = requests.put(url, headers=headers, json=data)
    
    
    # Check response status
    if response.status_code == 422:
        print("Error:", response.status_code, response.json())
    else:
        response.raise_for_status()

    return response.json().get('commit', {}).get('sha')

class CustomSafeLoader(yaml.SafeLoader):
    pass

# Override the default behavior for interpreting certain scalar values
# This prevents automatic conversion of 'on' and 'off' to True and False
CustomSafeLoader.add_constructor('tag:yaml.org,2002:bool',
                                 CustomSafeLoader.construct_yaml_str)

def get_yaml_content():
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{YAML_FILE_PATH}"
    response = requests.get(url, headers=headers)
    content = response.json()
    
    # Decode YAML content
    yaml_dict = base64.b64decode(content['content']).decode('utf-8').replace('true','on')
    # print(yaml_dict)
    # print(type(yaml_dict))

    # Use the custom loader to load the YAML content
    yaml_content = yaml.load(yaml_dict, Loader=CustomSafeLoader)
    # print("this is yaml_content", yaml_content)

    sha_hash = content['sha']
    return yaml_content, sha_hash



# def get_yaml_content():
#     url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{YAML_FILE_PATH}"
#     response = requests.get(url, headers=headers)
#     response.raise_for_status()
#     content = response.json()
    
#     # Decode YAML content and return along with SHA hash
#     return {
#         "content": yaml.safe_load(base64.b64decode(content['content'])),
#         "sha": content['sha']
#     }
# # def update_yaml_content(new_content):
# #     url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{YAML_FILE_PATH}"
# #     current_content = get_yaml_content()
# #     current_content.update(new_content)
# #     updated_content = yaml.dump(current_content)
# #     data = {
# #         "message": "Update YAML file",
# #         "content": base64.b64encode(updated_content.encode()).decode(),
# #         "sha": current_content['sha']
# #     }
# #     response = requests.put(url, headers=headers, json=data)
# #     response.raise_for_status()

# def update_yaml_content(updated_variables):
#     url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{YAML_FILE_PATH}"
#     current_content = get_yaml_content()
    
#     # Check if 'env' section exists, if not, create it
#     if 'env' not in current_content:
#         current_content['env'] = {}
    
#     # Update environment variables under 'env' section
#     env_section = current_content['env']
#     for key, value in updated_variables.items():
#         env_section[key] = value
    
#     # Dump the content without changing the format
#     updated_content = yaml.dump(current_content, default_flow_style=False)
    
#     # Encode and prepare data for API call
#     data = {
#         "message": "Update YAML file",
#         "content": base64.b64encode(updated_content.encode()).decode(),
#         "sha": current_content['sha']
#     }
    
#     # Send the update request
#     response = requests.put(url, headers=headers, json=data)
#     response.raise_for_status()



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    client = request.form['client']
    mode = request.form['mode']
    # files = request.form['files']
    files = request.form.getlist('files')
    # files_string = ' '.join(files)

    folder = 'Tests/'

    # Prepend the folder name to each filename
    files_with_path = [f'{folder}{file}' for file in files]

    # Join into a space-separated string for the command line
    files_string = ' '.join(files_with_path)



    # Update the YAML file with the new values
    commit_sha = update_yaml_content({'BASE_URL': client, 'SANITY': mode, 'FILES': files_string})
    print(commit_sha)
    time.sleep(30)

    # Fetch the latest workflow run for the commit
    run_id = get_run_id_for_commit(commit_sha)
    
    if run_id:
        url = f"https://github.com/{REPO_OWNER}/{REPO_NAME}/actions/runs/{run_id}"
        # If run_id is found, return it in the response
        # return jsonify({'message': 'Configuration submitted successfully!', 'run_id': run_id, 'url': url})
        return 'Action triggered and click on this link to see the status: ' + f'<a href="{url}" target="_blank">View Workflow Run</a>' + '<br> Note: You can download the test-reports.zip file in the artifact section to see the generated report.'
    else:
        return jsonify({'message': 'Configuration submitted, but run ID not found.'}), 404

    # return 'Configuration submitted successfully!'

def get_run_id_for_commit(commit_sha):
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/actions/runs"
    params = {'branch': 'main'}  # Adjust the branch if needed
    runs_response = requests.get(url, headers=headers, params=params)
    print("this is runs_response",runs_response)
    runs_response.raise_for_status()
    runs = runs_response.json()['workflow_runs']
    # print("this is runs",runs)

    for run in runs:
        print(run['head_sha'])
        if run['head_sha'] == commit_sha:
            return run['id']

    return None


if __name__ == '__main__':
    app.run(debug=True)
