#!/usr/bin/env python3

"""Console implementation contains the entry point
    of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ Defines the hbnb command interpreter.

    Args:
        prompt (hbnb): command to execute

    """
    __class_list = ["BaseModel"]
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit cmd loop"""
        return True

    def do_EOF(self, arg):
        """End of file signal to quit program"""
        return True

    def emptyline(self):
        """This method is called when nothing is entered
           into the shell
        """
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd("\n")

    def do_create(self, arg):
        """Create command to create a new instance of BaseModel, save it in a
        JSON file and prints the id.

        Attributes:
            arg (str): inputted line in command prompt
        """
        line = arg.split()
        if not self.verify_class(line):  # if anything not True
            return
        instance = eval(line[0] + '()')  # instance name e.g BaseModel()
        if isinstance(instance, BaseModel):  # checks if instance is BaseModel
            instance.save()
            print(instance.id)
        return

    def do_show(self, arg):
        """Show command that prints the string representation of an instance
        based on the class name and id.

        Attributes:
           args (str): inputted line in command prompt.
        """
        line = arg.split()
        if not self.verify_class(line):  # if dis returns anything not True
            return
        if not self.verify_id(line):  # if dis returns anything not True
            return
        key = '{}.{}'.format(line[0], line[1])  # gets the action and id
        objects = models.storage.all()
        print(objects[key])  # prints id objects

    def do_destroy(self, arg):
        """Destroy command that deletes an instance based on the class name
        and id. Save the change in JSON file.
        Attributes:
            args (str): inputted line in command prompt.
        """
        line = arg.split()
        if not self.verify_class(line):  # if dis returns anything not True
            return
        if not self.verify_id(line):  # if dis returns anything not True
            return
        key = '{}.{}'.format(line[0], line[1])  # gets the action and id
        objects = models.storage.all()
        del objects[key]
        models.storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances based
        or not on the class name.
        """
        line = arg.split()
        objects = models.storage.all()
        to_print = []
        if len(line) == 0:  # checking if no classname is inputted
            for v in objects.values():
                to_print.append(str(v))
        elif line[0] in HBNBCommand.__class_list:  # check if name in classname
            for k, v in objects.items():
                if line[0] in k:
                    to_print.append(str(v))
        else:
            print("** class doesn't exist **")
            return False
        print(to_print)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        """
        line = arg.split()
        if not self.verify_class(line):
            return
        if not self.verify_id(line):
            return
        if not self.verify_attribute(line):
            return
        objects = models.storage.all()
        key = '{}.{}'.format(line[0], line[1])
        setattr(objects[key], line[2], line[3])
        models.storage.save()

    @classmethod
    def verify_class(cls, line):
        """Function to verify inputted classname"""
        if len(line) == 0:  # checking if no classname is inputted
            print("** class name missing **")
            return False
        elif line[0] not in HBNBCommand.__class_list:
            print("** class doesn\'t exist **")
            return False
        return True

    def verify_id(line):
        """Static method to verify the id.
        """
        if len(line) < 2:  # checks if input has id
            print('** instance id missing **')
            return False
        objects = models.storage.all()
        key = '{}.{}'.format(line[0], line[1])  # gets the action and id
        if key not in objects.keys():  # checks if id in storage
            print('** no instance found **')
            return False
        return True

    def verify_attribute(line):
        """Static method to verify the attribute in inputted line.
        """
        if len(line) < 3:  # checks if input has an attr name
            print("** attribute name missing **")
            return False
        elif len(line) < 4:  # checks if attr name has a value
            print("** value missing **")
            return False
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
