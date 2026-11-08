# Personal task manager
![Static Badge](https://img.shields.io/badge/python-blue?logo=python&logoColor=white)

A simple task manager built with Python

## Feature
- Add multiple tasks
- Save tasks
- Load saved tasks
- Admin mode
- Set task priority

## Task priority
Each task can have one of these priority levels:
- low
- medium
- high

## Requirements
- Python
- Python-dotenv

## Project structure
```text
Personal_task_manager/
│   .env.example
│   .gitignore
│   main.py
│   README.md
│   requirements.txt
│   tasks.py
│
├───images/
│       demo.gif
│       screenshot_main.png
```

## Installation
Install the required packages:

```bash
python -m pip install -r requirements.txt
```

## Envoiroment setup
Create a `.env` file in the project folder.

Use `.env.example` as a template.

Add your admin password.

```env
ADMIN_PASSWORD=put_your_password_here
```
Replace `put_your_password_here` with your own admin password.

## Run the program
Run the main file
```bash
python main.py
```

## Screenshot
![personal_task_manager_screenshot](images\screenshot_main.png)

## Demo
![personal_task_manager_demo](images\demo.gif)