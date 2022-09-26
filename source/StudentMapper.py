import os
from source.Student import Student


class StudentMapper:
    __slots__ = ['__student']
    def __init__(this, student):
        """
        All mappers require a Student object stored inside to be able to function
        """
        this.__student = student
        
    
    def save(this):
        """
        saves the student object in the database
        """
        path = os.path.join(os.getcwd(), "students")
        
        if(not os.path.exists(path)):
            os.mkdir(path)
        
        path = os.path.join(path, str(this.__student.getId()) + ".student")
        
        if(os.path.exists(path)):
            print("ID already exists\n")
            return False
            
        with open(path, 'w') as file:
            file.write(this.__student.getName())
            file.write("\n")
            file.write(this.__student.getAge())
            
        print("Student was created succesfully\n")
        
    def get(this):
        """
        loads student info from database and creates then returns a student object
        """
        path = os.path.join(os.getcwd(), "students")
        path = os.path.join(path, str(this.__student.getId()) + ".student")

        if(not os.path.exists(path)):
            print("ID doesn't exist \n")
            return False

        with open(path, 'r') as file:
            this.__student.setName(file.readline().strip("\n"))
            this.__student.setAge(file.readline())
            
        return this.__student
        
    def delete(this):
        """
        deletes the student object from the database
        """
        path = os.path.join(os.getcwd(), "students")
        path = os.path.join(path, str(this.__student.getId()) + ".student")

        if(not os.path.exists(path)):
            print("ID doesn't exist")
            return False
        
        os.remove(path)
        
        print("Student was deleted successfully \n")
