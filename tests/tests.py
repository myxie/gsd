#!/usr/bin/env
#Getting Shit Done
#myxie 2016

import unittest 
import os
from gsd import get_gsd_directory
import projects

class TestUtilityMethods(unittest.TestCase):
        
    def test_get_gsd_directory(self):
        self.assertEqual(get_gsd_directory(), '~/Dropbox/GSD')

class TestProjectMethods(unittest.TestCase):
    
    def test_make_todo(self):
        gsd_directory = os.getcwd() #Faking gsd directory as the current directory
        project_name = 'folder'
        project_directory = '{0}/{1}'.format(gsd_directory, project_name)
        if not os.path.exists(project_directory):
        #Mini setup as make_todo requires the project directory to exist
            os.makedirs(project_directory)
        
        projects.make_todo(project_directory,project_name)
        self.assertTrue(os.path.exists('{0}/todo.gsd'.format(\
                            project_directory)))


    def test_make_archive(self):
        gsd_directory = os.getcwd() #Faking gsd directory as the current directory
        project_name = 'folder'
        project_directory = '{0}/{1}'.format(gsd_directory, project_name)
        if not os.path.exists(project_directory):
        #Mini setup as make_archive requires the project directory to exist
            os.makedirs(project_directory)

        projects.make_archive(project_directory,project_name)
        self.assertTrue(os.path.exists('{0}/archive.gsd'.format(\
                            project_directory)))

        return 0

    def test_make_links(self):
        gsd_directory = os.getcwd() #Faking gsd directory as the current directory
        project_name = 'folder'
        project_directory = '{0}/{1}'.format(gsd_directory, project_name)
        if not os.path.exists(project_directory):
        #Mini setup as make_links requires the project directory to exist
            os.makedirs(project_directory)

        projects.make_links(project_directory,project_name)
        self.assertTrue(os.path.exists('{0}/links.gsd'.format(\
                            project_directory)))

     
    def test_project_setup(self):
        gsd_directory = os.getcwd() #Faking gsd directory as current directory
        project_name = 'project_setup'
        project_directory = '{0}/{1}'.format(gsd_directory, project_name)
        if not os.path.exists(project_directory):
        #Mini setup as make_links requires the project directory to exist
            os.makedirs(project_directory)

        projects.project_setup(project_directory,project_name)
        self.assertTrue(os.path.exists(project_directory))
        return 0 

    def test_make_project(self):
        gsd_directory = os.getcwd()
        project_name = 'test_project'
        project_directory = '{0}/{1}'.format(gsd_directory, project_name)
        print project_directory
        projects.make_project(gsd_directory, project_name)
        self.assertTrue(os.path.exists(project_directory))
        self.assertTrue(os.path.exists('{0}/todo.gsd'.format(project_directory)))
        return 0  
    
if __name__ == '__main__':
    unittest.main()
