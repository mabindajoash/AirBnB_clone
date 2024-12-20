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
    class_list = ["User", "BaseModel", "Review",
                  "City", "State", "Amenity", "Place"]

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
            print("** class name missing **")
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

    def default(self, line):
        """Handles commands in the formart .all()"""
        classname = None
        if ".all()" in line:
            classname = line.split(".all()")[0]
            if classname in self.class_list:
                obj1 = FileStorage()
                data = obj1.all()
                instance_list = []
                for instance in data.values():
                    if instance.__class__.__name__ == classname:
                        instance_list.append(str(instance))
                print(instance_list)
            else:
                print("** class doesn't exist **")

        if ".count" in line:
            classname = line.split(".count")[0]
            if classname in self.class_list:
                obj1 = FileStorage()
                data = obj1.all()
                count = 0
                for instance in data.values():
                    if instance.__class__.__name__ == classname:
                        count = count + 1
                print(count)
            else:
                print("** class doesn't exist **")

        if ".show" in line:
            classname, class_id_1 = line.split(".show")
            class_id = class_id_1.strip('()"')
            if classname in self.class_list:
                obj1 = FileStorage()
                data = obj1.all()
                for key, value in data.items():
                    if key == f"{classname}.{class_id}":
                        print(value)
                        break
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

        if ".destroy" in line:
            classname, class_id_1 = line.split(".destroy")
            class_id = class_id_1.strip('()"')
            if classname in self.class_list:
                obj1 = FileStorage()
                data = obj1.all()
                for key, value in data.items():
                    if key == f"{classname}.{class_id}":
                        del data[key]
                        break
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

        if ".update" in line:
            classname, my_tuple = line.split(".update")
            my_tuple = (
                my_tuple.replace('"', '')
                        .replace('(', '').replace(')', '')
             )
            args = [arg.strip() for arg in my_tuple.split(",")]
            print(args)
            if len(args) == 3:
                class_id, name, att_value = args
            class_id.strip('\"')
            print(class_id)
            name.strip("\"")
            att_value.strip("\"")
            if classname in self.class_list:
                obj1 = FileStorage()
                data = obj1.all()
                for key, value in data.items():
                    if key == f"{classname}.{class_id}":
                        setattr(value, name, att_value)
                        obj1.save()
                        break
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

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
                    break
            if found_object is None:
                print("** no instance found **")
            else:
                print(found_object)

    def do_destroy(self, line):
        """destroy an instance"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
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
            print("** class name missing **")
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
