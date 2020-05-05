#!/usr/bin/python3
""" Program that Gather data from an API and Export to JSON """
import json
import requests
from sys import argv

if __name__ == "__main__":
    """ Program Entry point """
    empId = argv[1]
    int_id = int(empId)
    url_todo = 'https://jsonplaceholder.typicode.com/todos'
    url_user = 'https://jsonplaceholder.typicode.com/users'
    payload1 = {'userId': empId}
    payload2 = {'id': empId}

    req_todo = requests.get(url_todo, params=payload1)
    req_user = requests.get(url_user, params=payload2)

    # Getting the NUMBER_OF_DONE_TASKS and total tasks
    total_tasks = req_todo.json()
    # Employee name from users
    user_data = req_user.json()
    emp_name = user_data[0].get('username')
    for js in total_tasks:
        title_task = js.get('title')
        completed_task = js.get('completed')

    list_json = []

    dic = {"task": title_task,
           "completed": completed_task,
           "username": emp_name}
    list_json.append(dic)

    data_id = {int_id: list_json}

    with open('{}.json'.format(int_id), 'w') as file_json:
        json.dump(data_id, file_json)
