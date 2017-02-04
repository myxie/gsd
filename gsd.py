#!/usr/bin/env python
#Getting Shit Done 
#myxie 2016

import argparse 
import os
import sys

# gsd specific imports
from projects import make_project, delete_project
from tasks import create_task, archive_task, display_tasks
from utils import get_gsd_directory

#Global definitions
project_choices = os.listdir(get_gsd_directory())

#Where the main magic happens for running gsd on the command line

def list_handler(args):
    if args.list == 'all':
        available_projects = os.listdir(get_gsd_directory())
        if len(available_projects) == 0:
            print '='*80 + '\n' + 'No projects in gsd directory\n' + '='*80
        for project in available_projects:
            print '='*80
            print '[project] ' + project + ':\n'
            print '-'*80
            display_tasks(project)

    if args.list in project_choices:
        project = args.list
        print '='*80
        display_tasks(project) 
    
def project_handler(args):
    #Handles the subparsing from the commandline
    if args.project == 'add':
        new_project = raw_input("[gsd] Enter the name of a new project:\n")
        directory = get_gsd_directory()
        make_project(directory, new_project)
        return 0
    if args.project == 'remove':
        available_projects = os.listdir(get_gsd_directory())
        if len(available_projects) == 0:
            print 'No projects exist'
            return 0
        print 'Projects available: ' + str(available_projects) + '\n'
        directory = get_gsd_directory()
        project = raw_input("[gsd] Enter the project you want to remove:\n")
        delete_project(directory, project)
        return 0

def task_handler(args):
    if args.task == 'add':
        available_projects = os.listdir(get_gsd_directory())
        print 'Projects available: ' + str(available_projects) + '\n'
        project = raw_input("[gsd] Enter the project the task belongs too:\n")
        new_task = raw_input("[gsd] Enter the task you want added:\n")
        create_task(project, new_task) 
        return 0
    if args.task == 'remove':
        available_projects = os.listdir(get_gsd_directory())
        print 'Projects available: ' + str(available_projects) + '\n'
        project = raw_input("[gsd] Enter the project from which you want to remove a task:\n")
        archive_task(project)
        return 0

if __name__ == "__main__":
    #Basic argument parsing for command line use
    parser = argparse.ArgumentParser(prog='gsd',description= \
                'Command line client for Getting Shit Done process')
    cl_choices = ['all'] + project_choices
    parser.add_argument('-l', '--list',  choices=cl_choices, default='all', \
                help='Display a summary of tasks in all projects')

    parser.add_argument('-p','--project', choices=['add', 'remove'], \
                help='Project help' )
    parser.add_argument('-t', '--task', choices=['add', 'remove'], \
                help='Task Help')

    args = parser.parse_args()
    #TODO Handle logic for tasks, lists, etc (work out a 'switching protocol')
    if args.project:
        project_handler(args)
        sys.exit()

    if args.task:
        task_handler(args)
        sys.exit() 

    if args.list: 
        list_handler(args)
        sys.exit()
       


