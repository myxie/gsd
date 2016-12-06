#!/usr/bin/env
#Getting Shit Done
#myxie 2016

import unittest 
from gsd import get_gsd_directory

class TestUtilityMethods(unittest.TestCase):
    
    def test_get_gsd_directory(self):
        self.assertEqual(get_gsd_directory(), '~/Dropbox/GSD/')


if __name__ == '__main__':
    unittest.main()
