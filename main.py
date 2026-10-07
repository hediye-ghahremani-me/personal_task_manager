name = input("Enter your name : ")

print("Welcome,", name, "!")

tasks = []

while True:
    task = input("Enter a task or type ( out ) to finish: ")

    if task == "out":
        break

    tasks.append(task)

print("Your tasks:")

for task in tasks:
    print("-", task)