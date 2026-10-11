def add_task(tasks, task):
    tasks.append(task)


def show_tasks(tasks):
    for task in tasks:
        print("Task : ", task)

def mark_done(tasks, task):
    if task in tasks:
        tasks.remove(task)
        tasks.append(task + " - Done")
    else:
        print("Task not found !!!")

def delete_task(tasks, task):
    if task in tasks:
        tasks.remove(task)
    else:
        print("Task not found !!!")