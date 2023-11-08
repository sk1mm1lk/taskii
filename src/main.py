#!/usr/bin/env python3

tasks = []

def add_task(task_name):
    tasks.append(task_name)

def view_tasks():
    for task in tasks:
        print(task)

def add_task_prompt():
    task_name = input("[task name]> ")
    add_task(task_name)

commands = {'add':add_task_prompt, 'view':view_tasks}

def edit_mode():
    user_input = ''
    is_editing = True
    quit_commands = ['quit', 'exit', 'q']

    while is_editing:
        user_input = input('> ')

        if user_input in quit_commands:
            is_editing = False

        edit_command(user_input)

def edit_command(command_input):
    try:
        commands[command_input.strip()]()
    except KeyError:
        pass

if __name__ == '__main__':
    edit_mode()
