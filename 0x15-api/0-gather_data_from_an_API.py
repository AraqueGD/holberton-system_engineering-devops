#!/usr/bin/python3
if __name__ == "__main__":
    import requests
    from sys import argv
    user_id = argv[1]
    id_int = int(user_id)
    url_todo = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(id_int))
    url_user = requests.get(
        'https://jsonplaceholder.typicode.com/users?id={}'.format(id_int))

    js_todo = url_todo.json()
    js_user = url_user.json()

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
