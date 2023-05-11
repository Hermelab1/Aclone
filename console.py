#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def emptyline(self):
        """shouldn’t execute anything"""
        pass

    def do_quit(self, line):
        """quit command to  exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to  exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
~                           
