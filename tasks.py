#!/usr/bin/env
#Getting Shit Done
#myxie 2016

import os
from utils import get_gsd_directory, get_project_directory

def create_task(project, task):
    #Opens the todo.gsd in the project directory
#    project_directory = '{0}/{1}'.format(get_gsd_directory(), project)
    project_directory = get_project_directory(project)
    if os.path.exists(project_directory):
        todo_path = '{0}/tasks.gsd'.format(project_directory)
        if os.path.exists(todo_path):
            todo_file = open(todo_path, 'a')
            todo_file.write(task+'\n')
            todo_file.close()

def archive_task(project):
    project_directory = '{0}/{1}'.format(get_gsd_directory(), project)
    if os.path.exists(project_directory):
        todo_path = '{0}/tasks.gsd'.format(project_directory)
        if os.path.exists(todo_path):
            tasks = []
            f = open(todo_path)
            tasks = f.readlines()
            choice = None  
            for index, task in enumerate(tasks[1:], start=1): #ignore the first line; it is a comment
                print '[{0}] '.format(index) + task
            while(choice is None): 
                user_input= input("Select numbered task you want deleted\n")
                choice = user_input  #  
                if(choice >= len(tasks)): #value of choice should always be no. lines - 1
                    print 'Selected task is out of range'
                    choice = None 

            task_file = open(todo_path, 'w')
            for index, task in enumerate(tasks):
                if index != choice:
                    task_file.write(task)
            task_file.close()

                    
