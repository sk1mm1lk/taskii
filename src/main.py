#!/usr/bin/env python3

QUIT          = ['quit', 'exit', 'q']
NORMAL_PROMPT = '> '
EDIT_PROMPT   = '# '

tasks = []

def add_task(task_name):
    tasks.append(task_name)

def add_task_prompt():
    task_name = input(f'[task name]{EDIT_PROMPT}').strip()
    add_task(task_name)

def view_tasks():
    for task_id, task_name in enumerate(tasks):
        print(f'[{task_id}] {task_name}')

def swap_tasks(task_1_index, task_2_index):
    task_1_valid = task_1_index >= 0 and task_1_index < len(tasks)
    task_2_valid = task_2_index >= 0 and task_2_index < len(tasks)

    if task_1_valid and task_2_valid:
        temp_task = tasks[task_1_index]
        tasks[task_1_index] = tasks[task_2_index]
        tasks[task_2_index] = temp_task

def swap_tasks_prompt():
    try:
        task_1 = int(input(f'[task 1]{EDIT_PROMPT}').strip())
        task_2 = int(input(f'[task 2]{EDIT_PROMPT}').strip())
    except:
        print('task numbers were invalid')

    swap_tasks(task_1, task_2)

def tick_task(task_index):
    task_valid = task_index >= 0 and task_index < len(tasks)

    if task_valid:
        tasks[task_index] = "[DONE] " + tasks[task_index]
        swap_tasks(task_index, len(tasks)-1)

def tick_task_prompt():
    task_index = int(input(f'[task index]{NORMAL_PROMPT}').strip())
    tick_task(task_index)

def save(file_name):
    tasks_string = ''

    for task in tasks:
        tasks_string = tasks_string + task + '\n'

    with open(file_name, 'w') as file:
        file.write(tasks_string)

def save_prompt():
    file_name = input(f'[file name]{NORMAL_PROMPT}').strip()

    save(file_name)

def save_and_quit(file_name):
    save(file_name)
    quit()

def save_and_quit_prompt():
    save_prompt()
    quit()

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

normal_commands = {'help':help,
                   'view':view_tasks,
                   'edit':edit_mode,
                   'tick':tick_task_prompt,
                   'save':save_prompt,
                   'wq':save_and_quit_prompt}
edit_commands   = {'help':help,
                   'add':add_task_prompt,
                   'view':view_tasks,
                   'normal':normal_mode,
                   'swap':swap_tasks_prompt,
                   'save':save_prompt,
                   'wq':save_and_quit_prompt}

if __name__ == '__main__':
    normal_mode()
