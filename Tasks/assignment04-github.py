import os
from github import Github

repo_name = 'Tasks/assignment04-github.py'

def replace_and_commit(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    new_content = content.replace("Andrew", "Ana")

    with open(file_path, 'w') as file:
        file.write(new_content)

def commit_to_github(file_path, github_token, repo_name, commit_message):
    g = Github(github_token)
    repo = g.get_repo(repo_name)

    with open(file_path, 'r') as file:
        content = file.read()

    repo.create_file(file_path, commit_message, content)

if __name__ == "__main__":
    file_path = 'assignment04.txt'
    repo_name = 'Tasks/assignment04-github.py'
    commit_message = 'Replace "Andrew" with "Ana""'

    github_token = os.environ.get('GITHUB_ACCESS_TOKEN')

    if not github_token:
        print("GitHub access token not found. Please set the 'GITHUB_ACCESS_TOKEN' environment variable.")
    else:
        replace_and_commit(file_path)
        commit_to_github(file_path, github_token, repo_name, commit_message)
