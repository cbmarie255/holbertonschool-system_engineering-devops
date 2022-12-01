#!/usr/bin/python3
"""
    Exporting data to a CSV file.
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
    username = company_profile['username']

    # Exporting tasks to CSV.
    list_url = API_URL + 'todos/?userId={}'.format(employee_id)
    resonse_for_todos = requests.get(list_url)
    to_do_list = resonse_for_todos.text
    tasks = json.loads(to_do_list)
    csv_format = ""
    for person in tasks:
        csv_format += '"{}","{}","{}","{}"\n'.format(
                employee_id,
                username,
                person['completed'],
                person['title'])
    with open('{}.csv'.format(employee_id), 'w', newline='') as csv_file:
        csv_file.write(csv_format)
