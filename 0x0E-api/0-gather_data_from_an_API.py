#!/usr/bin/python3
"""
    Gathering data from an API.
"""
from sys import argv
import json
import requests


# Grab the employee!
employee_id = argv[1]
url = 'https://jsonplaceholder.typicode.com/users?id{}='.format(employee_id)
response_for_user = requests.get(url)
employee_data = response_for_user.text
company_profile = json.loads(employee_data)
name = company_profile[0].get('name')

# Grab the todo list!
list_url = 'https://jsonplaceholder.typicode.com/todos?users?Id{}='.format(employee_id)
resonse_for_todos = requests.get(list_url)
to_do_list = resonse_for_todos.text
tasks = json.loads(to_do_list)
completed_tasks = []
completed_tasks_count = 0
for task in tasks:
    if task.get('completed'):
        completed_tasks.append(task)
        completed_tasks_count += 1

# Print the output on command line.
print("Employee {} is done with tasks({}/{}): ".format(name, completed_tasks_count, len(tasks)))
for task in completed_tasks:
    print("\t {}".format(task.get('title')))
