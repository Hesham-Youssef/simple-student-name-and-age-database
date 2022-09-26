class Student:
    __slots__ = ['__id', '__name', '__age']
    def __init__(this, id):
        """
        All students must have ids same as their ids in the database.
        New students carry id equals 0 as they have no files in the database yet
        """
        this.__id = id
        

    #getters and setters
    def getId(this):
        return this.__id
    
    def getName(this):
        return this.__name
    
    def getAge(this):
        return this.__age
    
    def setName(this, name):
        this.__name = name
        
    def setAge(this, age):
        this.__age = age