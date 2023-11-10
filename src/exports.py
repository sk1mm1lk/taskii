#!/usr/bin/env python3

import tasks as ts
import parser as ps

tasks = None

def save(file_name):
    tasks_string = ''

    if tasks is None:
        return

    for task in tasks.tasks:
        tasks_string = tasks_string + task.name + '\n'

    with open(file_name, 'w') as file:
        file.write(tasks_string)

def save_prompt():
    file_name = input(f'[file name]> ').strip()

    save(file_name)

def save_and_quit(file_name):
    save(file_name)
    quit()

def save_and_quit_prompt():
    save_prompt()
    quit()

def load_file(file_name):
    try:
        with open(file_name, 'r') as file:
            file_contents = file.read()
    except FileNotFoundError:
        return

    if tasks is None:
        return

    for line in file_contents.split("\n"):
        if len(line) == 0:
            continue

        tasks.append(line.strip())

def load_file_prompt():
    file_name = input(f'[file name]> ').strip()

    load_file(file_name)

parser = ps.Parser('exports')
parser.command_dict = {'save':save_prompt,
                       'wq':save_and_quit_prompt,
                       'load':load_file_prompt}
