from tasks import show_tasks, save_tasks, load_tasks
from dotenv import load_dotenv
import os 

load_dotenv()

name = input("Enter your name : ")
print("Hello, ", name, "welcome to personal task manager !")

admin_mode = input("Do you want to enter admin mode ? yes/no ")
if admin_mode.lower() == "yes":
    admin_password = input("Enter admin password : ")
    if admin_password == os.getenv("ADMIN_PASSWORD"):
        print("Admin mode activated !")
    else:
        print("Wrong password !")

tasks = load_tasks()
count = int(input("How many tasks do you want to add ? : "))

for i in range(count):
    task_name = input("Enter a task : ") 
    priority = input("Enter priority : (low / medium / high) ").lower()
    task = {
        "name": task_name,
        "priority": priority
    }
    tasks.append(task)

show_tasks(tasks)
save_tasks(tasks)
