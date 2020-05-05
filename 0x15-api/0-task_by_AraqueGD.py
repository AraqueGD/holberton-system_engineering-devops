#!/usr/bin/python3
if __name__ == "__main__":
    import requests
    from sys import argv
    user_id = int(argv[1])
    url_todo = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id))
    url_user = requests.get(
        'https://jsonplaceholder.typicode.com/users?id={}'.format(user_id))

    try:
        js_todo = url_todo.json()
        js_user = url_user.json()
    except ValueError:
        print('Not Exists')

    if (js_todo and js_user):
        name_user = js_user[0].get('name')
        done_task = []
        for task in js_todo:
            if (task.get('completed') is True):
                done_task.append(task)

    print("Employee {} is done with tasks({}/{}):".format(name_user,
                                                          len(done_task), len(js_todo)))
    for title in done_task:
        print("\t {}".format(title.get('title')))
