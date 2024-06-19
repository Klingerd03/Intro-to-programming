# john = ('intro to comp', 12, 'Business', 'Freshman')
# print(john[0])
# print(john[1])
# print(john[2])
#
# #packing one more Tuple
# robert = ('Biology', 22, 'Business', 'Junior')
#
# #packing
# jane = ('intro to comp', 12, 'Accounting', 'Senior')
# will = ('intro to comp', 12, 'Chemistry', 'Senior')
#
# #create a list of these tuples
# class_roster = [john, robert, jane, will]
#
# print("The 0th based position in the class is ", class_roster[0])
# print(class_roster[3][2])
#
# #unpacking a tuple - assign the values of the tuple to a set of variables.
# (course, roll_num, major, year) = john  #class_roster[1]
# print("course name", course)
# print("roll num", roll_num)

#john[0] = "Smith"  #You get an error because you cannot change the value of a tuple.

# a=10
# b=23
# (b,a)=(a,b)
#
# a=10
# b=5
# print(a,b)
#
# #swap values of a, b and c, d
# temp = a
# a = b
# b = temp
# print(a,b)
#
# #swap using tuples
# (b,a) = (a,b)
# print(a,b)


#Exercise:
#swap 4 variables
# a = 3
# b = 7
# c = 5
# d = 9
# (a,b,c,d) = (d, c, a, b)
# print(a,b,c,d)


#Methods on Tuple

#Length of a tuple
# mytuple = ("apple", "banana", "cherry", "banana")
#
# print(len(mytuple))
#
# mytuple.count("banana")
#
# mytuple.index()
