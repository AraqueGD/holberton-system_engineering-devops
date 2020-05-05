#!/usr/bin/python3
""" Program that Gather data from an API """
if __name__ == "__main__":
    import requests
    from sys import argv
    import csv
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

    with open('{}.csv'.format(int_id), 'w') as file_task:
        style_write = csv.writer(
            file_task, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for write in total_tasks:
            style_write.writerow(
                [int_id, emp_name, write.get('completed'), write.get('title')])
