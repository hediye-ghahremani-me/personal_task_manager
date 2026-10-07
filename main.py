from tasks import add_task, show_tasks

name = input("Enter your name : ")

print("Welcome,", name, "!")

tasks = []

while True:
    task = input("Enter a task or type ( out ) to finish: ")

    if task == "out":
        break

    add_task(tasks, task)

print("Your tasks:")
show_tasks(tasks)