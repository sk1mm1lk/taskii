#!/usr/bin/env python3

'''
PRIORITY KEY
    0: unset
    1: can ignore
    2: low priority
    3: mid priority
    4: high priority
    5: top priority

TIME_EST KEY
    0: unset
    1: < 1 hour
    2: < half day
    3: < full day
    4: < week
    5: > week

DIFFICULTY KEY
    0: unset
    1: easy
    2: medium
    3: hard
'''

class Task():
    def __init__(self, id, task_name):
        self.id          = id
        self.name        = task_name
        self.description = ''
        self.priority    = 0 # 0 - 5
        self.due_date    = 'yyyy-mm-dd' # TODO set as todays date by default
        self.time_est    = 0 # 0 - 5
        self.tags        = [self.id]
        self.difficulty  = 0 # 0 - 3
        self.location    = ''
        ## Possibly add later:
        #self.attachments = ''
        #task_tracking   = ''
        #self.energy_required = 0 # 0 - 5

class Tasks():
    def __init__(self):
        self.task_count = 0
        self.tasks = []

    def add_task(self, task_name):
        self.task_count += 1
        self.tasks.append(Task(self.task_count, task_name))

    def remove_task(self, task_index):
        task_valid = task_index >= 0 and task_index < len(self.tasks)

        if task_valid:
            self.tasks.pop(task_index)

    def swap_tasks(self, task_1_index, task_2_index):
        # TODO changed from indices to task_id
        task_1_valid = task_1_index >= 0 and task_1_index < len(self.tasks)
        task_2_valid = task_2_index >= 0 and task_2_index < len(self.tasks)

        if task_1_valid and task_2_valid:
            temp_task           = self.tasks[task_1_index]
            self.tasks[task_1_index] = self.tasks[task_2_index]
            self.tasks[task_2_index] = temp_task

    def tick_task(self, task_index):
        task_valid = task_index >= 0 and task_index < len(self.tasks)

        if task_valid:
            current_task_name = self.tasks[task_index].name
            self.tasks[task_index].name = "[x] " + current_task_name
            self.swap_tasks(task_index, len(self.tasks)-1)
