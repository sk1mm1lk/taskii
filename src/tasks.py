#!/usr/bin/env python3

class Task():
    def __init__(self, task_name):
        self.name = task_name

class Tasks():
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        self.tasks.append(Task(task_name))

    def remove_task(self, task_index):
        task_valid = task_index >= 0 and task_index < len(self.tasks)

        if task_valid:
            self.tasks.pop(task_index)

    def swap_tasks(self, task_1_index, task_2_index):
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
