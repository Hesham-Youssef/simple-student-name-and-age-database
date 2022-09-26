class IO:
    def promptAction():
        """
        Method prompts one of the 3 operations and returns some indication
        """
        done  = False
        while not done:
            userAction = input("Enter the index of your action\n"
                "1. Create\n"
                "2. Delete\n"
                "3. get\n"
                "4. quit\n")
            if userAction in ['1', '2', '3', '4']:
                done = True
            else:
                print("Enter a valid choice\n")
        
        return userAction
                
        
    def promptStudentInfo():
        """
        Method prompts student name and age and returns them if valid
        """
        done  = False
        while not done:
            print("Enter the student info")
            name = input("Student name: ")
            
            if name == "":
                return False, False
            
            if name.isspace():
                print("Enter a valid name\n")
                continue
            
            age = input("Student age: ")
            
            if age == "":
                return False, False
            
            if not age.isdecimal():
                print("Enter a valid age\n")
                continue
            
            done = True
            
        return name, age

    def promptStudentID():
        """
        Method prompts id and returns it if valid
        """
        done  = False
        while not done:
            id = input("Enter student ID: ")
            
            if id == "":
                return False
            
            if not id.isdecimal():
                print("Enter a valid ID\n")
                continue
            
            done = True
            
        return id

        
    def showStudent(student):
        """
        Method formats then displays student info retrieved from the database
        """
                
        print("Student name: " + str(student.getName()))
        print("Student age: " + str(student.getAge()) + "\n")
