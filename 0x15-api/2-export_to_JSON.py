#!/usr/bin/python3
""" Program that Gather data from an API """
if __name__ == "__main__":
    import json
    import requests
    from sys import argv
    """ Program Entry point """
    empId = argv[1]
    int_id = int(empId)
    url_todo = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        int_id)
    url_user = 'https://jsonplaceholder.typicode.com/users?id={}'.format(
        int_id)

    req_todo = requests.get(url_todo)
    req_user = requests.get(url_user)

    # Getting the NUMBER_OF_DONE_TASKS and total tasks
    total_tasks = req_todo.json()
    done_tasks = []
    for task in total_tasks:
        if (task.get('completed') is True):
            done_tasks.append(task)

    # Employee name from users
    user_data = req_user.json()
    emp_name = user_data[0].get('name')
    for js in total_tasks:
        title_task = js.get('title')
        completed_task = js.get('completed')

    list_dict = []
    user_tasks = {}

    with open('{}.json'.format(empId), 'w') as json_file:
        for task in total_tasks:
            task_info = {}
            task_info['task'] = task.get('title')
            task_info['completed'] = task.get('completed')
            task_info['username'] = emp_name
            list_dict.append(task_info)
        user_tasks[empId] = list_dict
        info = json.dumps(user_tasks)
        json_file.write(info)
