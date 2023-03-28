#!/usr/bin/python3

import requests
from sys import argv


if __name__ == "__main__":

    # retrieves name
    api_url_user = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    data_api_user = requests.get(api_url_user)
    user_list = data_api_user.json()
    name = user_list["name"]

    # retrieves todos info from user id
    params = {"userId": argv[1]}
    api_url_todo = "https://jsonplaceholder.typicode.com/todos"
    data_api_todo = requests.get(api_url_todo, params=params)
    todo_list = data_api_todo.json()

    pending_tasks = 0

    for item in todo_list:
        if item["completed"] == True:
            pending_tasks += 1

    print(
        f"Employee {name} is done with tasks ({pending_tasks}/{len(todo_list)})")