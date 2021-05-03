#!/usr/bin/python3
""" Python script to export data in the CSV format. """
import csv
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
        username = item.get("username")

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

with open('{}.csv'.format(argv[1]), 'w') as file:
    dataFile = task.get('title')
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    for task in tasks:
        writer.writerow([argv[1],
                         username,
                         task.get("completed"),
                         task.get("title")])
