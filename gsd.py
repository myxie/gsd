#!/usr/bin/env
#Getting Shit Done 
#myxie 2016

import argparse 

#Where the main magic happens for running gsd on the command line

def get_gsd_directory():
    #TODO Read .json file for configuration information 
    return '~/Dropbox/GSD/' 

if __name__ == "__main__":
    #Basic argument parsing for command line use
    parser = argparse.ArgumentParser(description= \
                'Command line client for Getting Shit Done process')
    parser.add_argument('--summary', \
                help='Display a summary of tasks in all projects')
    parser.add_argument('-p', '--project', \
                help='Initialise a new project within the gsd directory', \
                    dest = 'project')
    parser.add_argument('-t', '--task', nargs=2, metavar=('TASK', 'PROJECT'),\
                help='Add a task to a project', dest='task')

    args = parser.parse_args()
    #'Switching' on the arguments presented to the CLI
    if args.summary:
    #TODO Replace with call to respective functionality
        x = 0
    elif args.project:
    #TODO Replace with call to respective functionality
        x = 0
    elif args.task:
    #TODO Replace with call to respective functionality
        x = 0 
