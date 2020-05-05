#!/usr/bin/python3
""" Program that Gather data from an API """
if __name__ == "__main__":
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

    print("Employee {} is done with tasks({}/{}):".format(
        emp_name, len(done_tasks), len(total_tasks)))
    for task in done_tasks:
        print("\t {}".format(task.get('title')))
