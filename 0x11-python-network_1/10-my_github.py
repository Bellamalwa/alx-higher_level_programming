#!/usr/bin/python3
"""
    Python script that takes GitHub credentials
    (username and password) and uses the GitHub API to display id
"""
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: ./10-my_github.py <username> <token>")
        sys.exit(1)

    username, token = sys.argv[1], sys.argv[2]

    # Make the request with Basic Authentication using your token
    response = requests.get('https://api.github.com/user', auth=(username, token))

    if response.status_code == 200:
        try:
            user_data = response.json()
            user_id = user_data.get('id')
            if user_id is not None:
                print(user_id)
            else:
                print("None")
        except ValueError:
            print("Invalid JSON response")
    else:
        print("None")
