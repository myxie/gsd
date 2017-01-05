#!/usr/bin/env
#Getting Shit Done
#myxie 2016

#This is where all the code for managing projects happens

# import standard python things
import os
import shutil
# import gsd-specific things
from utils import create_file

def make_project(directory, project):
    '''This function makes a standard project and its respective features 
    @param project: The name of the project (and directory being created)
    '''

    project_directory = '{0}/{1}'.format(directory, project) 
    if not os.path.exists(project_directory):
        os.makedirs(project_directory)
    project_setup(project_directory, project) 

def delete_project(directory, project):
    project_directory = '{0}/{1}'.format(directory, project)
    if not os.path.exists(project_directory):
        print '[gsd] Project does not exist\n'
        return 0
    else: 
        user_response = raw_input('[gsd] Are you sure you want to delete ' \
                    + project + ' at ' + project_directory  + '? (y/n)\n')
        if user_response == 'y':
            shutil.rmtree(project_directory)


def project_setup(directory,project):
    '''Function setups the project directory with todo, archive, downloads'''
    make_tasks(directory, project)
    make_archive(directory, project)
    make_links(directory, project)
    #make_downloads()

def make_tasks(directory,project):
    '''Function that creates a todo.gsd file if it doesn't exist
    @param directory: The project directory
    @param project: The name of the project
    '''
    retval = create_file('tasks', directory, project)
    return 0

def make_archive(directory, project):
    '''Function that opens a archive.gsd file if it doesn't exist
    @param directory: The project directory
    @param project: The name of the project
    '''

    create_file('archive', directory, project)
    return 0

def make_links(directory,project):
    '''Function that opens a links.gsd file if it doesn't exist
    @param directory: The project directory
    @param project: The name of the project
    '''
    create_file('links', directory, project)
    return 0

#Downloads support not required yet, will build this in when it is required 
def make_downloads():
    #TODO write functionality for this
    return 0
  

