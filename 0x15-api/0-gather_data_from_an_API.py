#!/usr/bin/python3
"""
Python scrip  for a given employee ID
"""
import requests
from sys import argv

if __name__ == "__main__":

    u = argv[1]
    user = requests.get("http://jsonplaceholder.typicode.com/users/" +
                        u).json()
    todos = requests.get("http://jsonplaceholder.typicode.com/todos?userId=" +
                         u).json()
    done = requests.get("http://jsonplaceholder.typicode.com/todos?userId=" +
                        u + "&completed=true").json()

    print("Employee {} is done with tasks({}/{}):"
          .format(user.get("name"), len(done), len(todos)))
    for task in done:
        print("\t " + task.get("title"))
