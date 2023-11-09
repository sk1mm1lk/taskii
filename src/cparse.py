#!/usr/bin/env python3

def get_command(command_string):
    return command_string.strip().split(' ')[0].strip()

def get_params(command_string):
    command_tokens = command_string.strip().split(' ')

    if len(command_tokens) <= 1:
        return []
    
    return command_tokens[1:]
