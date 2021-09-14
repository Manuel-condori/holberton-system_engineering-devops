#!/usr/bin/python3
"""
Python script to export data in the JSON forma
"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    u = argv[1]
    user = requests.get("http://jsonplaceholder.typicode.com/users/" +
                        u).json()
    todos = requests.get("http://jsonplaceholder.typicode.com/todos?userId=" +
                         u).json()

    userid = str(user.get("id"))
    with open(userid + ".json", "w") as jsonfile:
        username = user.get("username")
        userid = str(user.get("id"))
        tasklist = []
        for task in todos:
            taskdict = {"task": task.get("title"),
                        "completed": task.get("completed"),
                        "username": username}
            tasklist.append(taskdict)
        userdict = {userid: tasklist}
        json.dump(userdict, jsonfile)
