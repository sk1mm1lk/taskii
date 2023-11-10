#!/usr/bin/env python3

class Parser():
    def __init__(self, name):
        self.name = name
        self.command_dict = {}
        self.parsers = []
    
    def get_commands(self):
        return self.command_dict.keys()

    def get_command(self, command_string):
        return command_string.strip().split(' ')[0].strip()

    def get_params(self, command_string):
        command_tokens = command_string.strip().split(' ')

        if len(command_tokens) <= 1:
            return []
    
        return command_tokens[1:]
    
    def where_is(self, command):
        if command in self.command_dict.keys():
            return self

        for parser in self.parsers:
            parser_match = parser.where_is(command)
            if parser_match is not None:
                return parser_match

        return None

    def run(self, command_string):
        command = self.get_command(command_string)
        params  = self.get_params(command_string)

        # TODO implement commands that take arguments
        
        try:
            self.command_dict[command]()
        except: # TODO specific exception
            pass
