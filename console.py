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

    def do_quit(self,arg):
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
        if not self.verify_class(line): # if anything not True
            return
        instance = eval(line[0] + '()')
        if isinstance(instance, BaseModel):
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
        if not self.verify_class(line): # if dis returns anything not True
            return
        if not self,verify_id(line): # if dis returns anything not True
            return
        key = '{}.{}'.format(line[0], line[1]) # gets the first two words 
        objects = models.storage.all()
        print(objects[key]) # prints id objects


    @classmethod
    def verify_class(cls, line):
        """Function to verify inputted classname"""
        if len(line) == 0: # checking if no classname is inputted
            print("** class name missing **")
            return False
        elif line[0] not in HBNBCommand.__class_list:
            print("** class doesn\'t exist **")
            return False
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
