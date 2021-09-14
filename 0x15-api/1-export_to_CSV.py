#!/usr/bin/python3
"""
Python script to export data in the CSV
"""
import requests
from sys import argv

if __name__ == "__main__":

    u = argv[1]
    user = requests.get("http://jsonplaceholder.typicode.com/users/" +
                        u).json()
    todos = requests.get("http://jsonplaceholder.typicode.com/todos?userId=" +
                         u).json()

    userid = str(user.get("id"))
    with open(userid + ".csv", "w") as csvfile:
        username = user.get("username")
        userid = user.get("id")
        for task in todos:
            csvfile.write('"{}","{}","{}","{}"\n'.
                          format(userid, username, task.get("completed"),
                                 task.get("title")))
