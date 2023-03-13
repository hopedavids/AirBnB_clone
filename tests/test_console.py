#!/usr/bin/python3

import unittest
import sys
from ..console import BackendShell


class TestConsole(unittest.TestCase):
    ''' This class contains definitions for the console unit tests cases'''

    def test_backend_shell(self):
        ''' A defined method for the console unit tests cases'''
        self.assertTrue(BackendShell.do_EOF(self, True))
        self.assertTrue(BackendShell.do_quit(self, True))


if __name__ == "__main__":
    unittest.main()
