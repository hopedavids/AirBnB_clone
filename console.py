#!/usr/bin/python3

import sys
import cmd


class BackendShell(cmd.Cmd):
    intro = "<<Backend Interactive Console. Type help or ? to list commands>>"
    prompt = "(hbnb) "
    file = None

    def do_EOF(self, line):
        'End of file of the application'
        return True

    def do_quit(self, arg):
        'Quit the application here'
        return True


if __name__ == '__main__':
    BackendShell().cmdloop()
