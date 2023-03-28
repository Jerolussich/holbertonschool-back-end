#!/usr/bin/python3
"""Task 2 module"""

import requests
import json
from sys import argv


if __name__ == "__main__":

    # retrieves name
    api_url_user = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    user_list = requests.get(api_url_user).json()
    name = user_list["name"]

    # retrieves todos info from user id
    params = {"userId": argv[1]}
    api_url_todo = "https://jsonplaceholder.typicode.com/todos"
    todo_list = requests.get(api_url_todo, params=params).json()

    pending_tasks = 0

    with open(f"{argv[1]}.json", "w+") as file:

        new_dict = {argv[1]: []}

        for item in todo_list:

            completed_value_item = item["completed"]

            item.pop("id")
            item.pop("userId")
            item.pop("completed")

            item["task"] = item.pop("title")
            item["completed"] = completed_value_item
            item["username"] = name
            new_dict[argv[1]].append(item)

        file.write(json.dumps(new_dict))
