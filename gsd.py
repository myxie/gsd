#!/usr/bin/env
#Getting Shit Done 
#myxie 2016

import argparse 
import os
from projects import make_project
from tasks import create_task, archive_task, display_tasks
from utils import get_gsd_directory
#Where the main magic happens for running gsd on the command line

def list_handler(args):
    if args.list == 'all':
        available_projects = os.listdir(get_gsd_directory())
        for project in available_projects:
            print '='*80
            print project + ':\n'
            display_tasks(project)

    if args.list == 'project':
        available_projects = os.listdir(get_gsd_directory())
        print 'Projects available: ' + str(available_projects) + '\n'
        project = raw_input("[gsd] Project: ")
        print '='*80
        display_tasks(project) 
        x = 0 
    
def project_handler(args):
    #Handles the subparsing from the commandline
    if args.project == 'add':
        new_project = raw_input("[gsd] Enter the name of a new project:\n")
        directory = get_gsd_directory()
        make_project(directory, new_project)

def task_handler(args):
    if args.task == 'add':
        new_task = raw_input("[gsd] Enter the task you want added:\n")
        project = raw_input("[gsd] Enter the project the task belongs too:\n")
        print new_task, project
        create_task(project, new_task) 
        return 0
    if args.task == 'remove':
        project = raw_input("[gsd] Enter the project from which \
                you want to remove a task:\n")
        archive_task(project)
        return 0

if __name__ == "__main__":
    #Basic argument parsing for command line use
    parser = argparse.ArgumentParser(prog='gsd',description= \
                'Command line client for Getting Shit Done process')
    parser.add_argument('-l', '--list',  choices=['all', 'project'], \
                help='Display a summary of tasks in all projects')

    parser.add_argument('-p','--project', choices=['add', 'remove'], \
                help='Project help' )
    parser.add_argument('-t', '--task', choices=['add', 'remove'], \
                help='Task Help')

    args = parser.parse_args()
    #TODO Handle logic for tasks, lists, etc (work out a 'switching protocol')
    if args.list: 
        list_handler(args)

    if args.project:
        project_handler(args) 
    
    if args.task:
        task_handler(args)
    

