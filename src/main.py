#!/usr/bin/env python3

QUIT          = ['quit', 'exit', 'q']
NORMAL_PROMPT = '> '
EDIT_PROMPT   = '# '

tasks = []

def add_task(task_name):
    tasks.append(task_name)

def add_task_prompt():
    task_name = input(f'[task name]{EDIT_PROMPT}')
    add_task(task_name)

def view_tasks():
    for task in tasks:
        print(task)

def help():
    print("Normal mode commands:")
    for command in normal_commands.keys():
        print(f'  {NORMAL_PROMPT}{command}')

    print("Edit mode commands:")
    for command in edit_commands.keys():
        print(f'  {EDIT_PROMPT}{command}')

# -- Normal mode functions --

def normal_mode():
    try:
        print(is_editing)
    except:
        pass
    user_input = ''
    is_normal = True

    while is_normal:
        user_input = input(NORMAL_PROMPT)

        if user_input in QUIT:
            quit()

        normal_command(user_input)

def normal_command(command_input):
    try:
        normal_commands[command_input.strip()]()
    except KeyError:
        pass

# -- Edit mode functions --

def edit_mode():
    user_input = ''
    is_editing = True

    while is_editing:
        user_input = input(EDIT_PROMPT)

        if user_input in QUIT:
            quit()

        edit_command(user_input)

def edit_command(command_input):
    try:
        edit_commands[command_input.strip()]()
    except KeyError:
        pass

normal_commands = {'help':help, 'view':view_tasks, 'edit':edit_mode}
edit_commands = {'help':help, 'add':add_task_prompt, 'view':view_tasks, 'normal':normal_mode}

if __name__ == '__main__':
    normal_mode()
