#!/usr/bin/python3

import requests
import json
from sys import argv
import csv


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

    with open(f"{argv[1]}.csv", "w+") as file:
        for item in todo_list:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            writer.writerow([item['userId'],
                            name,
                            item['completed'],
                            item['title']])
