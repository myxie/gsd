#!/usr/bin/env
#Getting Shit Done
#myxie 2016

from utils import get_gsd_directory()

def create_task(project, task)
    #Opens the todo.gsd in the project directory
    project_directory = '{0}/{1}'.format(get_gsd_directory(), project)
    if.path.exists(project_directory):
        todo_path = '{0}/todo.gsd'.format(project_directory))
        if path.os.exists(todo_path):
            todo_file = open(todo_path, 'a')
            todo_file.write(task)
            todo_file.close()
