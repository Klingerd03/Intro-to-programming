# class Student:
#     name = ""
#     dob = ""
#     id = ""
#     major = ""

#main program starts here

#create an instance of this Student class.
# student1 = Student()   #Creating the object (an instance of this class)
#
# print(type(student1))

#assign values to the attributes of this class
# student1.name = "smith"
# student1.dob = "1/1/1990"
# student1.id = "au123"
# print(student1.name, student1.dob, student1.id) #checking the newly assigned attributes.

#Creating another object of the same class:
# student2 = Student()   #giving it a meaningful name
# student2.name = "Bob"


#Creating a new class, create instances (objects) of class, assign values, then display.
# class Automobile:
#     brand = ""
#     year = ""
#     miles = ""
#
# Car = Automobile()
# Truck = Automobile()
# SUV = Automobile()
#
# Car.brand = "Ford"
# Car.year = "1999"
# Car.miles = "225000"
#
# Truck.brand = "Ford"
# Truck.year = "2024"
# Truck.miles = "500"
#
# SUV.brand = "Jeep"
# SUV.year = "2020"
# SUV.miles = "55000"
#
# print(Car.brand, Car.year, Car.miles)
# print(Truck.brand, Truck.year, Truck.miles)
# print(SUV.brand, SUV.year, SUV.miles)

#The CONSTRUCTOR function:
class Student:
    def __init__(self, name, dob, id, major): #these are the arguments for this function.
        self.name = name #assigning the value of the argurment called name to the attribute 'name'.
        self.dob = dob
        self.id = id
        self.major = major

#create an object of the Student class by CALLING its constructor w/ values for the attributes.
student1 = Student('John', '1/1/2000', 'AU123', 'compsci')
print(student1.name, student1.dob)
student2 = Student('Bill', '12/10/2000', "AU345", 'compsci')
student3 = Student('Bob', '2/20/2001', "AU678", 'compsci')
print(student2.name, student2.dob)
print(student3.name, student3.dob)

#try to change the name of a student
student1.name = "Rob"
print(student1.name)

