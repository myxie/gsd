#!/usr/bin/env
#Getting Shit Done
#myxie 2016

#This is where all the code for managing projects happens

# import standard python things
import os
# import gsd-specific things
from gsd import get_gsd_directory

def make_project(directory, project):
    '''This function makes a standard project and its respective features 
    @param project: The name of the project (and directory being created)
    '''

    project_directory = '{0}/{1}'.format(directory, project) 
    print project_directory
    if not os.path.exists(project_directory):
        os.makedirs(project_directory)
    project_setup(project_directory, project) 

def project_setup(directory,project):
    '''Function setups the project directory with todo, archive, downloads'''
    make_todo(directory, project)
    make_archive(directory, project)
    make_links(directory, project)
    #make_downloads()

def make_todo(directory,project):
    '''Function that creates a todo.gsd file if it doesn't exist
    @param directory: The project directory
    @param project: The name of the project
    '''

    if os.path.exists(directory):
        todo_path = '{0}/todo.gsd'.format(directory)
        if not os.path.exists(todo_path):
            todo_file = open(todo_path, 'w') 
            todo_file.write('#Todo list for the {0} project'.format(project)) 
            todo_file.close()
    else:
        return -1 #Not good; it should have been created in make_project()

    return 0

def make_archive(directory, project):
    '''Function that opens a archive.gsd file if it doesn't exist
    @param directory: The project directory
    @param project: The name of the project
    '''

    if os.path.exists(directory):
        archive_path = '{0}/archive.gsd'.format(directory)
        if not os.path.exists(archive_path):
            todo_file = open(archive_path, 'w') 
            todo_file.write('#Archived tasks from the {0} project'.format(project)) 
            todo_file.close()
    else:
        return -1 #Not good; it should have been created in make_project()

    return 0

def make_links(directory,project):
    '''Function that opens a links.gsd file if it doesn't exist
    @param directory: The project directory
    @param project: The name of the project
    '''

    if os.path.exists(directory):
        links_path = '{0}/links.gsd'.format(directory)
        if not os.path.exists(links_path):
            todo_file = open(links_path, 'w') 
            todo_file.write('#Links for the {0} project'.format(project)) 
            todo_file.close()
    else:
        return -1 #Not good; it should have been created in make_project()

    return 0

#Downloads support not required yet, will build this in when it is required 
def make_downloads():
    #TODO write functionality for this
    return 0
  

