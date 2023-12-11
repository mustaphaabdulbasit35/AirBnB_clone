#!/usr/bin/python3
"""Here we are defining the actual console, using the cmd module
Don't forget implementing commands"""
import re
import cmd
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State


class HBNBCommand(cmd.Cmd):
    """
    This is the class that defines our console, it represents the
    commands that can be executed by our command line interpreter
    Attributes:
        prompt(hbnb): represents the prompt of our command line interpreter
    """
    prompt = "(hbnb) "
    __defined_classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def default(self, arg):
        """
        Shows the default behaviour of our module when user input
        is not accurate
        """
        arg_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        arg_match = re.search(r"\.", arg)
        if arg_match is not None:
            arg_list = [arg[:arg_match.span()[0]], arg[arg_match.span()[1]:]]
            arg_match = re.search(r"\((.*?)\)", arg_list[1])
            if arg_match is not None:
                user_command = [arg_list[1][:arg_match.span()[0]], arg_match.group()[1:-1]]
                if user_command[0] in arg_dict.keys():
                    call = "{} {}".format(arg_list[0], user_command[1])
                    return arg_dict[user_command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False
    
    def emptyline(self):
        """WE can do nothing when nothing has been entered by the user"""
        pass

    def do_create(self, arg):
        """
        Creates a new class instance and follows up with showing its ID.
        """
        arg_list = parse_command(arg)
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.__defined_classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg_list[0])().id)
            storage.save()

    def do_quit(self, arg):
        """
        command used to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF is used to indicate End Of File
        """
        print("")
        return True
    
    def do_destroy(self, arg):
        """
        Destroys <class> <id> or <class>.destroy(<id>)
        Will delete the created class of a defined ID.
        """
        arg_list = parse_command(arg)
        object_dict = storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.__defined_classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in object_dict.keys():
            print("** no instance found **")
        else:
            del object_dict["{}.{}".format(arg_list[0], arg_list[1])]
            storage.save()

    def do_show(self, arg):
        """
        Shows class <id> or <class>.show(<id>)
        Display the string representation of a class instance, given the ID.
        """
        arg_list = parse_command(arg)
        object_dict = storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.__defined_classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in object_dict:
            print("** no instance found **")
        else:
            print(object_dict["{}.{}".format(arg_list[0], arg_list[1])])

    def do_count(self, arg):
        """
        count <class> or <class>.count()
        counts and gives the number of instances of a given class.
        """
        arg_list = parse_command(arg)
        cnt = 0
        for objct in storage.all().values():
            if arg_list[0] == objct.__class__.__name__:
                cnt += 1
        print(cnt)

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not
        on the class name
        If no class is specified, displays all instantiated objects.
        """
        arg_list = parse_command(arg)
        if len(arg_list) > 0 and arg_list[0] not in HBNBCommand.__defined_classes:
            print("** class doesn't exist **")
        else:
            object_list = []
            for objct in storage.all().values():
                if len(arg_list) > 0 and arg_list[0] == objct.__class__.__name__:
                    object_list.append(objct.__str__())
                elif len(arg_list) == 0:
                    object_list.append(objct.__str__())
            print(object_list)

    def do_update(self, arg):
        """
         Updates an instance based on the class name and id
         by adding or updating attribute(save the change into the JSON file)
        """
        arg_list = parse_command(arg)
        object_dict = storage.all()

        if len(arg_list) == 0:
            print("** class name missing **")
            return False
        if arg_list[0] not in HBNBCommand.__defined_classes:
            print("** class doesn't exist **")
            return False
        if len(arg_list) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg_list[0], arg_list[1]) not in object_dict.keys():
            print("** no instance found **")
            return False
        if len(arg_list) == 2:
            print("** attribute name missing **")
            return False
        if len(arg_list) == 3:
            try:
                type(eval(arg_list[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arg_list) == 4:
            objct = object_dict["{}.{}".format(arg_list[0], arg_list[1])]
            if arg_list[2] in objct.__class__.__dict__.keys():
                value_type = type(objct.__class__.__dict__[arg_list[2]])
                objct.__dict__[arg_list[2]] = value_type(arg_list[3])
            else:
                objct.__dict__[arg_list[2]] = arg_list[3]
        elif type(eval(arg_list[2])) == dict:
            objct = object_dict["{}.{}".format(arg_list[0], arg_list[1])]
            for key, value in eval(arg_list[2]).items():
                if (key in objct.__class__.__dict__.keys() and
                        type(objct.__class__.__dict__[key]) in {str, int, float}):
                    value_type = type(objct.__class__.__dict__[key])
                    objct.__dict__[key] = value_type(value)
                else:
                    objct.__dict__[key] = value
        storage.save()


def parse_command(arg):
    """
    Function to parse user commands, to ensure correct execution
    """
    located_braces = re.search(r"\{(.*?)\}", arg)
    located_brackets = re.search(r"\[(.*?)\]", arg)
    if located_braces is None:
        if located_brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:located_brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(located_brackets.group())
            return retl
    else:
        lexer = split(arg[:located_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(located_braces.group())
        return retl


if __name__ == "__main__":
    HBNBCommand().cmdloop()