#!/usr/bin/python3
"""
Python script to export data in the JSON format
"""
import json
import requests

if __name__ == "__main__":

    users = requests.get("http://jsonplaceholder.typicode.com/users").json()
    with open("todo_all_employees.json", "w") as jsonfile:
        usertaskdict = {}
        for userid in users:
            username = userid.get("username")
            userid = str(userid.get("id"))
            todos = requests.get("http://jsonplaceholder.typicode.com/todos?" +
                                 "userId=" + userid).json()

            tasklist = []
            for task in todos:
                taskdict = {"task": task.get("title"),
                            "completed": task.get("completed"),
                            "username": username}
                tasklist.append(taskdict)
            usertaskdict[userid] = tasklist
        json.dump(usertaskdict, jsonfile)
