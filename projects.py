#!/usr/bin/env
#Getting Shit Done
#myxie 2016

#This is where all the code for managing projects happens

# import standard python things
from os import mkdir
# import gsd-specific things
from gsd import get_gsd_directory

def make_project(project):
   '''This function makes a standard project and its respective features 

   @param project: The name of the project (and directory being created)

   ''' 
   
    gsd_directory = get_gsd_directory()
    project_directory = '{0}/{1}'.format(gsd_directory, project) 
    mkdir(project_directory)
    project_setup(project_directory) 

def project_setup(directory):
    #TODO Function setups all the relevant files within the project directory
    '''Function setups the project directory with todo, archive, downloads'''
    make_todo()
    make_archive()
    make_downloads()
    return 0

def make_todo():
    #TODO write functionatlity for this 
    return 0 

def make_archive()
    #TODO write functionality for this
    return 0

def make_downloads()
    #TODO write functionality for this
    return 0
  

