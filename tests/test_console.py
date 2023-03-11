#!/usr/bin/python3

import unittest
import sys
sys.path.append('../')
from console import BackendShell


class TestConsole(unittest.TestCase):

    def test_backend_shell(self):
        self.assertTrue(BackendShell.do_EOF(self, True))
        self.assertTrue(BackendShell.do_quit(self, True))


if __name__ == "__main__":
    unittest.main()