#!/usr/bin/python3
""" Python script using REST API for a given
employee ID, returns information about TODO list progress """
import requests
from sys import argv


if __name__ == "__main__":
    todos = requests.get("https://jsonplaceholder.typicode.com/todos/",
                         params={"user_id": argv[1]})
    users = requests.get("https://jsonplaceholder.typicode.com/users/",
                         params={"user_id": argv[1]})
    tasks = todos.json()
    user = users.json()
    for item in user:
        name = item.get("name")
    task_end = 0
    for task in tasks:
        if task.get("completed"):
            task_end += 1
    print("Employee {} is done with tasks({}/{}:".format(name,
                                                         task_end,
                                                         len(tasks)))
    for title in tasks:
        if title.get("completed"):
            print("\t {}".format(title.get("title")))
