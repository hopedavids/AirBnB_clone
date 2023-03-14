#!/usr/bin/python3

import sys
import cmd
import BaseModel

class HBNBCommand(cmd.Cmd):
    """This is a the backend interactive shell interface"""
    intro = "<<Backend Interactive Console. Type help or ? to list commands>>"
    prompt = "(hbnb) "
    file = None
    classes = {'BaseModel': BaseModel}

    def do_create(self, line):
        """Creates a new instances of BaseModel, saves it (to the JSON file) and prints the id"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes[class_name]()
        new_instance.save()
        print(new_instance.id) 

    def do_EOF(self, line):
        # An End of File command to close the open file
        'End of file of the application'
        return True

    def do_quit(self, arg):
        # A Quit command to close the shell program
        'Quit command to exit the program'
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
