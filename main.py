from tasks import show_tasks

name = input("Enter your name : ")
print("welcome, ", name, "!")

tasks = []
count = int(input("How many tasks do you want to add ? : "))

for i in range(count):
    task = input("Enter a task : ") 
    tasks.append(task)

show_tasks(tasks)