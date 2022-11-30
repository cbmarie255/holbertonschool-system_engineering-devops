#!/usr/bin/python3
"""
    Gathering data from an API.
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    API_URL = 'https://jsonplaceholder.typicode.com/'
    # Grab the employee!
    employee_id = argv[1]
    url = API_URL + 'users/{}'.format(employee_id)
    response_for_user = requests.get(url)
    company_profile = json.loads(response_for_user.text)
    name = company_profile['name']

    # Grab the todo list!
    list_url = API_URL + 'todos/?userId={}'.format(employee_id)
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
    prompt_1 = "Employee {} is done with ".format(name)
    prompt_2 = "tasks({}/{}):".format(completed_tasks_count, len(tasks))
    print(prompt_1 + prompt_2)
    for to_do in completed_tasks:
        print("\t {}".format(to_do.get('title')))
