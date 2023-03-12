#!/usr/bin/python3

import sys
import cmd


class BackendShell(cmd.Cmd):
    """This is a the backend interactive shell interface"""
    intro = "<<Backend Interactive Console. Type help or ? to list commands>>"
    prompt = "(hbnb) "
    file = None

    def do_EOF(self, line):
        # An End of File command to close the open file
        'End of file of the application'
        return True

    def do_quit(self, arg):
        # A Quit command to close the shell program
        'Quit the application here'
        return True


if __name__ == '__main__':
    BackendShell().cmdloop()
