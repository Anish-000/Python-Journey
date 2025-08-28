# Object oriented programming in python --------------------------------------------------------------->
# class & objects ----------------->

class Student : 
    name = " Anish "

s1 = Student()                  # s1 is object
print(s1.name)

# Constructor -------------->
# _init_ function --------->

class SStudent :
    name = " Ani "
    def __init__(self) :                # Default constructor
        print(self)
        print(" Adding new Names ")

s1 = SStudent()
print(s1)

# Now adding New Names ---->
class Classroom :
    def __init__(self,name) :           # self parameter is a reference to the current instance of the class
        self.name = name                # Parameterized constructor

s1 = Classroom(" Anish ")
s2 = Classroom(" Shrestha ")

print(s1.name)
print(s2.name)

# Precidence of object attribute is greater than precidence of class attribute 
# example ---->
class Cars :
    name = " Toyota "
    def __init__(self,name) :
        self.name = name

s1 = Cars(" BMW ")
print(s1.name)

# defining Method in class ---->
class Lang :
    def __init__ (self, name, marks) :
        self.name = name
        self.marks = marks
    
    def display(self) :
        print("Language Name : ", self.name)
    
    def getmarks(self) :
        return self.marks

    @staticmethod                       # Decorator 
    def hello():                        # static method ( we are not using self as parameter)
        print("Hello, World!")
    
s1 = Lang("C++", 95.4)
s1.hello()
s1.display()
print(s1.getmarks())

# Create a class named Student1 that takes name and marks of 3 subjects as arguments in constructor.
# Then create a method to print the avg.

class S :
    def __init__(self, name , marks) :
        self.name = name
        self.marks = marks
    
    def getAvg(self) :
        sum = 0
        for val in self.marks :
            sum += val
        
        avg = sum/3
        return avg

s1 = S("Anish", [99, 98, 97])
print(s1.name, ",", " Your Average is : ", s1.getAvg())

