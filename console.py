#!/usr/bin/python3
"""
Module containing class HBNBCommand
"""


from models.user import User
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.place import Place
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """entry point of the command interpreter"""
    class_list = ["User", "BaseModel", "Review", "City", "State", "Amenity", "Place"]

    prompt = "(hbnb)"

    def do_quit(self, line):
        """quit the prompt"""
        return True

    def do_EOF(self, line):
        """in case of ctrl c"""
        return True

    def emptyline(self):
        """empty line executes the previous command"""
        pass

    def do_create(self, line):
        """create new instance and save to json file"""
        if not line:
            print ("** class name missing **")
        elif line not in self.class_list:
            print("** class doesn't exist **")
        elif line == "BaseModel":
            object1 = BaseModel()
            object1.save()
            print(f"{object1.id}")
        elif line == "User":
            object1 = User()
            object1.save()
            print(object1.id)
        elif line == "City":
            object1 = City()
            object1.save()
            print(object1.id)
        elif line == "State":
            object1 = State()
            object1.save()
            print(object1.id)
        elif line == "Amenity":
            object1 = Amenity()
            object1.save()
            print(object1.id)
        elif line == "Place":
            object1 = Place()
            object1.save()
            print(object1.id)
        elif line == "Review":
            object1 = Review()
            object1.save()
            print(object1.id)

    def do_show(self, line):
        """print an instance"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.class_list:
            print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id missing **")
        else:
            object1 = FileStorage()
            data = object1.all()
            found_object = None
            for key, value in data.items():
                if key == f"{args[0]}.{args[1]}":
                    found_object = value
                    break;
            if found_object is None:
                print("** no instance found **")
            else:
                print(found_object)

    def do_destroy(self, line):
        """destroy an instance"""
        args = line.split()
        if len(args) == 0:
            print("** class name is missing **")
        elif args[0] not in self.class_list:
            print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id missing **")
        else:
            found_key = None
            object1 = FileStorage()
            data = object1.all()
            for key, value in data.items():
                if key == f"{args[0]}.{args[1]}":
                    found_key = key
                    break
            if found_key is None:
                print("** no instance found **")
            else:
                del data[found_key]
                object1.save()

    def do_all(self, line):
        """print all instances"""
        if len(line) != 0 and line not in self.class_list:
            print("** class doesn't exist **")
        else:
            object1 = FileStorage()
            data = object1.all()
            obj_list = [str(value) for key, value in data.items()]
            print(obj_list)

    def do_update(self, line):
        """destroy an instance"""
        args = line.split()
        if len(args) == 0:
            print("** class name is missing **")
        elif args[0] not in self.class_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            object1 = FileStorage()
            data = object1.all()
            for key, value in data.items():
                if key == f"{args[0]}.{args[1]}":
                    setattr(value, args[2], args[3])
                    break
            else:
                print("** no instance found **")
            object1.save()














if __name__ == '__main__':
    HBNBCommand().cmdloop()
