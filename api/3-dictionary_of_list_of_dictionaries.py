#!/usr/bin/python3
"""Task 3 module"""

import requests
import json
from sys import argv


if __name__ == "__main__":

    # retrieves name
    api_url_user = f"https://jsonplaceholder.typicode.com/users/"
    user_list = requests.get(api_url_user).json()

    # retrieves todos info from all users
    api_url_todo = "https://jsonplaceholder.typicode.com/todos"
    todo_list = requests.get(api_url_todo).json()

    relevant_data_list = []
    new_dict = {}

    # formats data tuple and prepares dict
    for item in user_list:
        data_tuple = (item["id"], item["username"])
        relevant_data_list.append(data_tuple)

    for item in relevant_data_list:
        new_dict[item[0]] = []

    with open(f"todo_all_employees.json", "w+") as file:

        item_dict = {}

        for item in todo_list:

            for data_tuple in relevant_data_list:
                if item["userId"] == data_tuple[0]:
                    name = data_tuple[1]

            item_dict["username"] = name
            item_dict["task"] = item["title"]
            item_dict["completed"] = item["completed"]

            new_dict[item["userId"]].append(item_dict)

        file.write(json.dumps(new_dict))
