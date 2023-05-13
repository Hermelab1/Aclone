#!/usr/bin/python3

import cmd
import sys
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """A class to difine an hbnb command"""
    prompt = "(hbnb)"

    def emptyline(self):
        """shouldn’t execute anything"""
        pass

    def do_quit(self, args):
        """quit command to  exit the program"""
        return True

    def do_EOF(self, args):
        """EOF command to  exit the program"""
        return True

    def help_quit(self):
        """print help message to quit"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """print help message to EOF"""
        print("EOF command to exit th program")

    def do_create(self, args):
        """Create instance BaseModel, saves to JSON file & prints id."""
        if not agrs:
            print("** class name missing **")
            return

        try:
            new_instance = eval(args)()
            new_instance.save()
            print(new_instance)

        except NameError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
