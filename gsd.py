#!/usr/bin/env
#Getting Shit Done 
#myxie 2016

import argparse 
import os
from projects import make_project
from tasks import create_task,archive_task
from utils import get_gsd_directory
#Where the main magic happens for running gsd on the command line

def project_handler(args):
    #Handles the subparsing from the commandline
    if args.add:
        directory = get_gsd_directory()
        project = args.add[0] 
        make_project(directory, project)
    elif args.list:
        x = 0 

def task_handler(args):
    if args.add:
        if not args.project:
            print '--project option also required when adding a task'
            return -1
        task = ' '.join(args.add) #Creates a string from the task arguments
        print task
        project = args.project[0]
        create_task(project, task) 
        return 0
    if args.remove:
        if not args.project:
            print '--project option also required when removing a task'
            return -1
        project = args.project[0]
        print project
        archive_task(project)
        return 0

if __name__ == "__main__":
    #Basic argument parsing for command line use
    parser = argparse.ArgumentParser(prog='gsd',description= \
                'Command line client for Getting Shit Done process')
    parser.add_argument('--summary', \
                help='Display a summary of tasks in all projects')

    subparsers = parser.add_subparsers(title='subcommands',help='Sub Commands',\
                dest='subparser_name')
    parser_project = subparsers.add_parser('project', help='Project help' )
    parser_project.add_argument('-a', '--add', nargs=1, \
                help='Initialise a new project within the gsd directory') 
    parser_project.add_argument('-l', '--list', nargs=1, \
                help='List the tasks for a specific project')
    parser_project.set_defaults(func=project_handler)

    parser_task = subparsers.add_parser('task', help='Task help')
    parser_task.add_argument('-a', '--add', nargs='+',type=str, metavar='TASK',\
                help='Add a task to a project' )
    parser_task.add_argument('-p', '--project', nargs=1, type=str, \
                help='Project to which the task is being added') 
    parser_task.add_argument('--remove', action='store_true', \
                help='Remove a task from a project')
    parser_task.set_defaults(func=task_handler)

    args = parser.parse_args()
    args.func(args)
