#/usr/bin/env
#Getting Shit Done
#myxie 2016

import os
from utils import get_gsd_directory, get_project_directory

def create_task(project, task):
    #Opens the todo.gsd in the project directory
    project_directory = get_project_directory(project)
    if os.path.exists(project_directory):
        todo_path = '{0}/tasks.txt'.format(project_directory)
        if os.path.exists(todo_path):
            todo_file = open(todo_path, 'a')
            todo_file.write(task+'\n')
            todo_file.close()

def archive_task(project):
    project_directory = '{0}/{1}'.format(get_gsd_directory(), project)
    if os.path.exists(project_directory):
        todo_path = '{0}/tasks.txt'.format(project_directory)
        archive_path = '{0}/archive.txt'.format(project_directory)
     
        if os.path.exists(todo_path):
            tasks = []
            f = open(todo_path, 'r')
            tasks = f.readlines()
            f.close()
            choice = None  

            if len(tasks) <= 1:
                print '[gsd] There are no tasks to remove'
                return 0
            for index, task in enumerate(tasks[1:], start=1): #ignore the first line; it is a comment
                print '[{0}] '.format(index) + task

            while(choice is None): 
                user_input= raw_input("[gsd] Select numbered task you want deleted\n")
                #TODO find a way to cater for multiple options e.g. 1 2 3 7
                choice = int(user_input)  #raw_input is a string  
                if(choice >= len(tasks)): #value of choice should always be no. lines - 1
                    print '[gsd] Selected task is out of range'
                    choice = None 
        
            #Write tasks to back to file and ommit task chosen for removal
            task_file = open(todo_path, 'w')
            for index, task in enumerate(tasks):
                if index != choice:
                    task_file.write(task)
            task_file.close()

            #Write the removed task to the archive file
            archive_file = open(archive_path, 'a') 
            archive_file.write(tasks[choice] + '\n')
            archive_file.close()
            
    else:
        print '[gsd] Project or project path does not exist'


def display_tasks(project):
    project_directory = '{0}/{1}'.format(get_gsd_directory(), project)
    if os.path.exists(project_directory):
        todo_path = '{0}/tasks.txt'.format(project_directory)
        if os.path.exists(todo_path):
            tasks = []
            f = open(todo_path, 'r')
            tasks = f.readlines()
            for task in tasks[1:]:
                print '[task] ' + task
    else:
        print 'Project directory does not exist'
