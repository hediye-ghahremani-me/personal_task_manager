from tasks import add_task, show_tasks, mark_done, delete_task
from dotenv import load_dotenv
import os

load_dotenv()
admin_password = os.getenv("TASK_MANAGER_ADMIN_PASSWORD")

open_admin = input("Do you want to enter Admin Mode? (yes/no): ")

if open_admin.lower == "yes":
    entered_password = input("Enter admin password: ")

    if entered_password == admin_password:
        print("Hi, admin...")

    else:
        print("Wrong password !")

name = input("Enter your name : ")

print("Welcome,", name, "!")

tasks = []

while True:
    task = input("Enter a task or type (out) to finish: ").lower()

    if task == "out":
        break

    priority = input("Enter priority ( low/medium/high ): ")

    while priority not in ["low", "medium", "high"]:
        print("Invalid priority! Please enter low, medium or high...")
        priority = input("Enter priority ( low/medium/high ): ")

    task = task + " - " + priority

    add_task(tasks, task)

while True:
    choice = input("Do you want your task (any of them) to get done or delete ? type (out) to exit : ").lower()

    if choice == "done":
        task = input("Enter full task: ")
        mark_done(tasks, task)

    elif choice == "delete":
        task = input("Enter full task: ")
        delete_task(tasks, task)

    elif choice == "out":
        break

print("Your tasks:")
show_tasks(tasks)

with open("tasks.txt", "a") as file:
    file.write(f"name: {name}, tasks: {tasks}")