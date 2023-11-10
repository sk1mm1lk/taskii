#!/usr/bin/env python3

import tasks as ts
import parser as ps

tasks = None

def examplefunc():
    print('This is merely and example function')

parser = ps.Parser('example')
parser.command_dict = {'examplefunc':examplefunc}
