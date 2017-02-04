#!/usr/bin/env
#Getting Shit Done
#myxie 2016

#Utility functions for gsd project
import os

def get_gsd_directory():
    #TOOD Read.json file for configuration information
    return '/home/croutons/github/gsd/demonstration_directory'

def get_project_directory(project):
    return '{0}/{1}'.format(get_gsd_directory(), project) 

def create_file(file_type, directory, project):
    if os.path.exists(directory):
        file_path = '{0}/{1}.gsd'.format(directory, file_type)
        if not os.path.exists(file_path):
            output = open(file_path, 'w')
            output.write('#{0} for the {1} project\n'.format(file_type, project))
            output.close()
            return 0
    else:
        return -1 #Not good; it should have been created in make_project()
