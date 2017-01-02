#!/usr/bin/env
#Getting Shit Done
#myxie 2016

import unittest 
import os
import shutil
from utils import get_gsd_directory, create_file
import projects
import tasks
class TestUtilityMethods(unittest.TestCase):
        
    def test_get_gsd_directory(self):
        self.assertEqual(get_gsd_directory(), '/home/croutons/Dropbox/GSD')
    
    def test_create_file(self):
        file_type = 'test'
        project = 'create_project_mark_ii'
        current_directory = os.getcwd()
#        directory = '/home/croutons/Dropbox/GSD/create_project'
        gsd_directory = get_gsd_directory()       
        directory = gsd_directory + '/' + project 
        if not os.path.exists(directory):
            os.makedirs(directory)
        create_file(file_type, directory,project)
        required_directory = '{0}/{1}.gsd'.format(directory, file_type)
        self.assertTrue(os.path.exists(required_directory))

class TestProjectMethods(unittest.TestCase):
    
    def test_make_tasks(self):
        gsd_directory = get_gsd_directory() 
        project_name = 'folder'
        project_directory = gsd_directory + '/' + project_name 
        if not os.path.exists(project_directory):
        #Mini setup as make_todo requires the project directory to exist
            os.makedirs(project_directory)
        
        #create_file('task', project_directory, project_name)
        projects.make_tasks(project_directory,project_name)
        required_file = project_directory + '/tasks.gsd'
        self.assertTrue(os.path.exists(required_file))

        shutil.rmtree(project_directory)

    def test_make_archive(self):
        gsd_directory =  get_gsd_directory() #Faking gsd directory as the current directory
        project_name = 'folder'
        project_directory = '{0}/{1}'.format(gsd_directory, project_name)
        if not os.path.exists(str(project_directory)):
        #Mini setup as make_archive requires the project directory to exist
            os.makedirs(project_directory)

        projects.make_archive(project_directory,project_name)
        self.assertTrue(os.path.exists('{0}/archive.gsd'.format(\
                            str(project_directory))))

        shutil.rmtree(project_directory)

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

        shutil.rmtree(project_directory)       
     
    def test_project_setup(self):
        gsd_directory = os.getcwd() #Faking gsd directory as current directory
        project_name = 'project_setup'
        project_directory = '{0}/{1}'.format(gsd_directory, project_name)
        if not os.path.exists(project_directory):
        #Mini setup as make_links requires the project directory to exist
            os.makedirs(project_directory)

        projects.project_setup(project_directory,project_name)
        self.assertTrue(os.path.exists(project_directory))
        
        shutil.rmtree(project_directory)  
        return 0 

    def test_make_project(self):
        gsd_directory = get_gsd_directory()
        project_name = 'test_project'
        project_directory = '{0}/{1}'.format(gsd_directory, project_name)
        projects.make_project(gsd_directory, project_name)
        self.assertTrue(os.path.exists(project_directory))
        self.assertTrue(os.path.exists('{0}/tasks.gsd'.format(project_directory)))

        shutil.rmtree(project_directory)
        return 0  

class TestTaskMethods(unittest.TestCase):
    
    def test_create_task(self):
        project = 'task_create_project'
        gsd_directory = get_gsd_directory()
        projects.make_project(gsd_directory, project)
        taska = 'Pick up the milk on the way home'
        tasks.create_task(project, taska)
        taskb = 'Drink the milk when you get home'
        tasks.create_task(project, taskb)
        return 0
    
    def test_archive_task(self):
        project = 'archive_task_project'
        gsd_directory = get_gsd_directory()
        project_directory = '{0}/{1}'.format(gsd_directory, project) 
        if os.path.exists(project_directory):
            shutil.rmtree(project_directory)
        projects.make_project(gsd_directory, project)
        taska = 'This is an example task 1' 
        taskb = 'This is an example task 2' 
        tasks.create_task(project, taska)
        tasks.create_task(project, taskb)
        tasks.archive_task(project)
         
        return 0

if __name__ == '__main__':
    unittest.main()
