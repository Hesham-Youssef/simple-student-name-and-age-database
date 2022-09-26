import os
from source.IO import IO
from source.StudentMapper import StudentMapper
from source.Student import Student

        
if __name__ == '__main__':
    done = False
    while not done:
        action = IO.promptAction()
        if(action == '4'):
            break
        while True:
            if action == '1':
                name , age = IO.promptStudentInfo()
                if(not name):
                    break
                id = IO.promptStudentID()
                if(not id):
                    break
                student = Student(id)
                student.setName(name)
                student.setAge(age)
                StudentMapper(student).save()
                
            elif action == '2':  
                id = IO.promptStudentID()
                if(not id):
                    break
                student = Student(id)
                student = StudentMapper(student).delete()
                    
                 
            elif action == '3':
                id = IO.promptStudentID()
                if(not id):
                    break
                student = Student(id)
                student = StudentMapper(student).get()
                if(student == False):
                    continue
                
                IO.showStudent(student)
                    
                
    