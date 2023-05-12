#!/usr/bin/python3
"""
contains entry point of our command interpreter
"""
import cmd
import sys
import models
from typing import List
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    """command interpreter class"""

    prompt = "(hbnb) "
    __classes = ["User", "Amenity", "City", "Place", "Review", "State"]

    def do_quit(self, args):
        """quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """EOF command to exit the program"""
        return True

    def emptyargs(self):
        """empty args should not excecute anything"""
        pass

    def do_create(self, args: List[str]):
        """creates a new instance of BaseModel saves it to json file and prints the id"""
        args = args.split()  # ['User'] -> User()
        if not args:  # checks if class name is missing
            print("**class name missing**")
            return
        # check if class name doesn't exist in the program
        elif args[0] not in HBNBCommand.__classes:
            print("**class name doesn't exist**")
        else:
            # create new instance of baseModel
            new_instance = eval(args[0] + "()")
            for arg in args[1:]:
                if "=" in arg:
                    key, value = arg.split("=")
                    value = value.replace("_", " ")
                    try:
                        value = int(value)
                    except ValueError:
                        try:
                            value = float(value)
                        except ValueError:
                            value = value.strip('"').replace('\\"', '"')
                    setattr(new_instance, key, value)
            # save it to json file
            print(new_instance)
            new_instance.save()
            # print id of new_instance
            print(new_instance.id)

    def do_show(self, args):
        """shows the string representation of an instance based on the class name and id (show <class name> <instance ID>)"""
        args = args.split()
        if len(args) == 0:
            print("**class name missing**")
            return
        elif args[0] not in HBNBCommand.__classes:
            print("**class doesn't exist**")
            return
        elif len(args) == 1:
            print("**instance id missing**")
            return
        else:
            # This args retrieves a dictionary of all instances of all classes stored in a JSON file using the all() method of the storage module
            objects = models.storage.all()
            # creates a key to look up the instance in the object dictionary
            key = "{}.{}".format(args[0], args[1])
            if key not in objects:
                print("**no instance found**")
                return
            # print the string representation of the instance to the console
            print(objects[key])

    def do_destroy(self, args):
        """
        deletes an instance based on the class name and id provided then stores the changes to the json file
        """
        args = args.split()
        if len(args) == 0:
            print("**class name missing**")
            return
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist")
            return
        elif len(args) == 1:
            print("**instance id missing**")
            return
        else:
            # using the all() method of the storage module to retrieve a dictionary of all objects stored in json file
            objects = models.storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key not in objects:
                print("**no instance found**")
                return
            del objects[key]  # delete the instance from the dictionary
            models.storage.save()  # save changes to the json file

    def do_all(self, args):
        """prints string representation of objects"""
        my_dict = (
            models.storage.all()
        )  # retrieves all objects currently stored in the models.storage dictionary and assigns them to the my_dict variable.
        args = args.split()
        my_list = []
        if not args:  # if args is an empty string
            for keys, values in my_dict.items():
                my_list.append(str(values))
            print(my_list)
        else:
            for value in my_dict.values():
                # checks if the class name of the instance matches the argument passed to the all command
                if value.to_dict()["__class__"] == args[0]:
                    # if match is found append the string representation ofthe  object to my_list
                    my_list.append(str(value))
            if not my_list:
                print("**class doesn't exist**")
            else:
                print(my_list)

    def do_update(self, args):
        """
        updates an instance based on the class name and id by adding or updating attribute then save changes into json file
        Usage: update <class name> <id> <attribute name> "<attribute value>
        """
        args = args.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        elif len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
        # create a key to search for instance in dictionary
        key = args[0] + "." + args[1]
        if key not in models.storage.all().keys():
            print("** no instance found **")
            return
        # get the instance from the dictionary using our key
        instance = models.storage.all()[key]
        # set the attribute value for the instance
        setattr(instance, args[2], args[3])
        models.storage.save()  # save changes to json file


if __name__ == "__main__":
    HBNBCommand().cmdloop()
