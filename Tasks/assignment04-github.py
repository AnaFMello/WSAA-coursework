pip install GitPython
import os
import subprocess

def replace_and_commit(file_path, old_text, new_text):
    # Read the content of the file
    with open(file_path, 'r') as file:
        content = file.read()

    # Replace all instances of old_text with new_text
    modified_content = content.replace(old_text, new_text)

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.write(modified_content)

    # Commit the changes using Git
    commit_message = f"Replace {old_text} with {new_text}"
    subprocess.run(['git', 'add', file_path])
    subprocess.run(['git', 'commit', '-m', commit_message])
    subprocess.run(['git', 'push'])

if __name__ == "__main__":
    # Specify the file path, old text, and your name
    file_path = 'Tasks/assignment04-github.py'
    old_text = 'Andrew'
    your_name = 'Ana'

    # Call the function to replace and commit changes
    replace_and_commit(file_path, old_text, your_name)
