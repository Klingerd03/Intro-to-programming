#Exercise:
#Write a function that returns the sum of three number
#Write a function that takes a number and returns its cube
#Write a function that takes a name (a string) and returns "Hello <name>"

#1
def add (a, b, c):
    sum = a + b + c
    return sum

# a=10
# b=3
# c=21
# print(add(a,b,c))

#2
def cube (x):
    num = x**3
    return num

#test:
# x = 5
# print(cube(x))

#3
def HelloName (string1):
    return print(f'Hello {string1}')

#test:
# name = input()
# HelloName(name)



#Exercise: Using a module for a Class:
#Create a module that has the following class definition:
#Student:
#Attributes -Fname, Lname, Major
#Getter and setter methods

#Def a function in this module - call it sum_of_list(list)
#Returns the sum

#Import this module into another file
#Create a few objects of the class and test the getter and setter methods
#Test the function sum_of_lists()

class Student:
    def __init__(self, fname, lname, major):
        self.fname = fname
        self.lname = lname
        self.major = major

    def get_fname(self):
        return self.fname