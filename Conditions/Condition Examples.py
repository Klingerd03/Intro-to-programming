#Exercise 1

# var1 = 20
# var2 = 13
# var3 = 8
#
# #check if a is greater than b and if it is greater than, print the value of a.
#
# if (var1 > var2):
#     print("This is the value of var1", var1)
#
# print ("This is the value of var2", var2)
# print ("This is the value of var3", var3)

#Exercise 2

# var1 = 15
# var2 = 10
# #check if var1 is greater than var2 and if it is greater than, print "var1 is greater than var2".
#
# if (var1 > var2):
#     print ("var1 is greater than var2")

#Exercise 3
#
# Num1 = 10
# #if Num1 is even, square it and print the result
#
# if (Num1%2 == 0):
#     print(Num1**2)

# #Exercise 4   UNFINISHED
#
# Num2 = 14
# #see if number is divisible by 7, if not then print it's value, otherwise print it's square.
#
# if Num2%2 == 0:
#     print()
# else:
#     print(Num2**2)


#Exercise 5
# use input to get an integer from the user and then determine if the number is even or odd.
# Print an output that lets the user know if the number is even or odd.
#
# int1 = int(input("What is your integer?"))
#
# if int1%2 == 0:
#     print("This number is even.")
# else:
#     print("This number is odd.")

#Exercise 6: elif
#
# weekday = int(input("Provide a number from 0 to 6"))
#
# if weekday == 0:
#     print("Sunday")
# elif (weekday == 1):
#     print("Monday")
# elif (weekday == 2):
#     print("Tuesday")
# elif (weekday == 3):
#     print("Wednesday")
# elif (weekday == 4):
#     print("Thursday")
# elif (weekday == 5):
#     print("Friday")
# elif (weekday == 6):
#     print("Saturday")
# else:
#     pass

#Exercise 7: nested elif

#Write a program to find the greatest of three numbers using if-else stmts.
#
# num1 = 1
# num2 = 2
# num3 = 3
# num4 = 4
#
# if(num1 > num2):
#     if(num1 > num3):
#         print("The first number is the greatest.")
#     if(num2 > num3):
#         print("The second number is the greatest.")
# elif (num2 > num3:
#     print("The third number is the greatest.")

#
# if (num1 > num2 and num1 > num3 and num1 > num4):
#     print("The first number is the greatest.")
# elif (num2 > num1 and num2 > num3 and num2 > num4):
#     print("The second number is the greatest.")
# elif (num3 > num1 and num3 > num2 and num3 > num4):
#     print("The third number is the greatest.")
# else:
#     print("The fourth number is the greatest.")
#

#Exercise 8: OR

number = int(input("Enter a number"))

if number%5 == 0 or number%7 == 0:
    print("You are a winner")
    if number%8 == 0:
        print("You are a super winner")
else:
    print("Number is not divisible by 5 or 7")
