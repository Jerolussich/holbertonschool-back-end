import requests
from sys import argv


def dataGatherer():
    # retrieves name
    api_url_user = "https://jsonplaceholder.typicode.com/users/{}".format(
        argv[1])
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

    print("Employee {} is done with tasks ({}/{}).".format(name,
          pending_tasks, len(todo_list)))


if __name__ == "__main__":
    dataGatherer()
