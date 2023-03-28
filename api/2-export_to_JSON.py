#!/usr/bin/python3
"""
Module 2-export_to_json
"""
from json import dump
import requests
from sys import argv


if __name__ == '__main__':

    user_id = int(argv[1])

    resp = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(user_id))
    username = resp.json().get('username')

    resp = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id))

    tasks = {}
    tasks.setdefault(user_id, [])
    for task in resp.json():
        tasks[user_id].append(dict(task=task['title'],
                                   completed=task['completed'],
                                   username=username))

    with open(str(user_id) + '.json', 'w') as file:
        dump(tasks, file)
