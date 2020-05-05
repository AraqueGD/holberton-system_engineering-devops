#!/usr/bin/python3
if __name__ == "__main__":
    import requests
    from sys import argv
    user_id = argv[1]
    int_id = int(user_id)
    url_todo = 'https://jsonplaceholder.typicode.com/todos?userId=' + user_id
    url_user = 'https://jsonplaceholder.typicode.com/users?id=' + user_id

    r_todo = requests.get(url_todo)
    r_user = requests.get(url_user)

    try:
        js_todo = r_todo.json()
        js_user = r_user.json()
    except ValueError:
        print('Not Exists JSON')

    name_user = js_user[0].get('name')
    done_task = []
    for task in js_todo:
        if (task.get('completed') is True):
            done_task.append(task)

    print("Employee {:s} is done with tasks({:d}/{:d}):".format(name_user,
                                                                len(done_task), len(js_todo)))
    for title in done_task:
        print("\t {}".format(title.get('title')))
