#!/usr/bin/env python3

import tasks as ts
import basecli
import exports

QUIT          = ['quit', 'exit', 'q']
NORMAL_PROMPT = '> '
EDIT_PROMPT   = '# '

module_commands = [basecli.commands, exports.commands]
module_parsers  = [basecli.parser,   exports.parser]

tasks = ts.Tasks()

basecli.tasks = tasks
exports.tasks = tasks

def help():
    print("Normal mode commands:")
    for command in normal_commands.keys():
        print(f'  {NORMAL_PROMPT}{command}')

    print("Edit mode commands:")
    for command in edit_commands.keys():
        print(f'  {EDIT_PROMPT}{command}')

# -- Normal mode functions --

def normal_mode():
    user_input = ''
    is_normal = True

    while is_normal:
        user_input = input(NORMAL_PROMPT)

        if user_input in QUIT:
            quit()

        run_command(user_input)

def run_command(command_string):
    stripped_string = command_string.strip()
    command         = stripped_string.split(' ')[0].strip()

    module_index = match_command(command)

    if module_index >= 0:
        module_parsers[module_index](stripped_string)

def match_command(command):
    if command == 'help':
        for command_set in module_commands:
            for option in command_set:
                print(f'- {option}')
        return -1

    for module_index, module_data in enumerate(module_commands):
        if command in module_data:
            return module_index

    return -1

if __name__ == '__main__':
    normal_mode()
