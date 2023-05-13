#!/usr/bin/python3
"""
HBNB Console Models
"""

import cmd
import sys
import re
from shlex import split
from models import storage
from models.base_model import BaseModel


def parse(args):
    """To difine Parse"""
    curly_braces = re.search(r"\{(.*?)\}", args)
    brackets = re.search(r"\[(.*?)\]", args)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(args)]
        else:
            lexer = split(args[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(args[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """HBNB class"""
    prompt = "(hbnb)"

    classes = {'BaseModel': BaseModel}

    def emptyline(self):
        """shouldn’t execute anything"""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

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
        print("EOF command to exit the program")

    def do_create(self, args):
        """Create instance BaseModel, saves to JSON file & prints id."""
        argslength = parse(args)
        if len(argslength) == 0:
            print("** class name missing **")
        elif argslength[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argslength[0])().id)
            storage.save()

    def do_show(self, args):
        """to show the string representation of a class instance"""
        argslen = parse(args)
        obdic = storage.all()
        if len(arglen) == 0:
            print("** class name missing **")
        elif argslen[0] not in HBNBCommand.__classes:
            print("** class doen't exist **")
        elif len(argslen) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argslen[0], argslen[1]) not in obdic:
            print("** no instance found **")
        else:
            print(obdic["{}.{}".format(argslen[0], argslen[1])])

    def do_destroy(self, args):
        """to delete an instance based on the class name and id"""
        argslen = parse(args)
        obdic = storage.all()
        if len(argslen) == 0:
            print("** class name missing **")
        elif argslen[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argslen) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argslen[0], argslen[1]) not in obdic.keys():
            print("** no instance found **")
        else:
            del obdic["{}.{}".format(argslen[0], argslen[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        argl = parse(arg)
        if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_update(self, args):
        """A defination to update an instance based on class name & id"""
        argl = parse(args)
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
