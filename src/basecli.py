#!/usr/bin/env python3

import tasks as ts
import cparse as cpar

NORMAL_PROMPT = '> '
EDIT_PROMPT   = '# '

tasks = None

def add_task_prompt():
    task_name = input(f'[task name]{EDIT_PROMPT}').strip()

    if tasks is not None:
        tasks.add_task(task_name)

def remove_task_prompt():
    try:
        task_index = int(input(f'[task 1]{EDIT_PROMPT}').strip())
    except ValueError:
        print('task index is invalid')
        return

    if tasks is not None:
        tasks.remove_task(task_index)

def view_tasks():
    if tasks is None:
        return

    for task_id, task in enumerate(tasks.tasks):
        print(f'[{task_id}] {task.name}')

def swap_tasks_prompt():
    try:
        task_1 = int(input(f'[task 1]{EDIT_PROMPT}').strip())
        task_2 = int(input(f'[task 2]{EDIT_PROMPT}').strip())
    except ValueError:
        print('task indices were invalid')
        return

    if tasks is not None:
        tasks.swap_tasks(task_1, task_2)

def tick_task_prompt():
    task_index = int(input(f'[task index]{NORMAL_PROMPT}').strip())
    
    if tasks is not None:
        tasks.tick_task(task_index)

command_dict = {'add':add_task_prompt,
                'remove':remove_task_prompt,
                'view':view_tasks,
                'swap':swap_tasks_prompt,
                'tick':tick_task_prompt}
commands     = command_dict.keys()

def parser(command_string):
    command = cpar.get_command(command_string)
    params  = cpar.get_params(command_string)

    # TODO implement commands that take arguments
    
    command_dict[command]()
