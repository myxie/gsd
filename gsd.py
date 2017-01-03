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
    print 'In project Handler'
    if args.project == 'add':
        new_project = raw_input("Enter the name of a new project")
        directory = get_gsd_directory()
        make_project(directory, new_project)
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
    parser.add_argument('--list', \
                help='Display a summary of tasks in all projects')

    parser.add_argument('-p','--project', choices=['add', 'list'], \
                help='Project help' )
    parser.add_argument('-t', '--task', choices=['add', 'remove'], \
                help='Task Help')

    args = parser.parse_args()
    #TODO Handle logic for tasks, lists, etc (work out a 'switching protocol')
    if args.project:
        print args        
        project_handler(args) 


