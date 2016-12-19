#!/usr/bin/env
#Getting Shit Done 
#myxie 2016

import argparse 
import os
from projects import make_project
#Where the main magic happens for running gsd on the command line

def get_gsd_directory():
    #TODO Read .json file for configuration information 
    return '/home/croutons/Dropbox/GSD' 

if __name__ == "__main__":
    #Basic argument parsing for command line use
    parser = argparse.ArgumentParser(description= \
                'Command line client for Getting Shit Done process')
    parser.add_argument('--summary', \
                help='Display a summary of tasks in all projects')
    parser.add_argument('-p', '--project', nargs=1, metavar='PROJECT', \
                help='Initialise a new project within the gsd directory', \
                    dest = 'project')
    parser.add_argument('-t', '--task', nargs=2, metavar=('TASK', 'PROJECT'),\
                help='Add a task to a project', dest='task')
    parser.add_argument('-i', '--inspect', nargs=1, metavar=('PROJECT'), \
                help='Inspect the tasks for a specific project', dest='inspect')
    args = parser.parse_args()
    
    #Get a summary of all project tasks
    if args.summary:
    #TODO Replace with call to respective functionality
        x = 0

    #Add a project
    elif args.project:
        print args.project[0]
        directory = get_gsd_directory()
        project = args.project[0] 

        make_project(directory, project)

    elif args.task:
    #TODO Replace with call to respective functionality
        x = 0 
