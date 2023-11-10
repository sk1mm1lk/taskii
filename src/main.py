#!/usr/bin/env python3

import tasks as ts
import basecli
import exports
import parser as ps

QUIT          = ['quit', 'exit', 'q']
NORMAL_PROMPT = '> '
EDIT_PROMPT   = '# '

def help():
    for parser in parsers.parsers:
        print(f'---{parser.name}---')
        for option in parser.get_commands():
            print(f'- {option}')
    return None

# -- Normal mode functions --

def normal_mode():
    user_input = ''
    is_normal = True

    while is_normal:
        user_input = input(NORMAL_PROMPT).strip()

        if user_input in QUIT:
            quit()

        run_command(user_input)

def run_command(command_string):
    stripped_string = command_string.strip()
    command         = stripped_string.split(' ')[0].strip()

    module  = parsers.where_is(command)

    if module is not None:
        try:
            module.run(stripped_string)
        except: # TODO proper exception
            pass

parsers = ps.Parser('main')
parsers.command_dict = {'help':help}
parsers.parsers = [basecli.parser,
                   exports.parser]

tasks = ts.Tasks()
basecli.tasks = tasks
exports.tasks = tasks

if __name__ == '__main__':
    normal_mode()
