#Two ways to do the same thing
# product *= 2
# product = product * 2
#
# index -= 1 # it will decrease by one each time
# index = index - 1

#Exercise:
# countdown = 10
# while countdown >0:
#     print(countdown)
#     countdown = countdown-1
# print("Blastoff")

#Exercise:
# sum = 0
# num = 1
# while num < 101:
#     sum = sum + num
#     num = num + 1
#     print(num)
# print(sum)


#Exercise:
#Create a list of all even numbers between 0 and 100 using while loop.
# even = []
# num = 0
# while num < 101:
#     if num%2 == 0:
#         even.append(num)
#     num += 1
# print(even)


#Exercise:
#The factorial of a number is the product of all the numbers up to that number.
#So factorial 4 = 1*2*3*4.
#Write a while loops to find the factorial of a number.
#Use input statement to get the number.

num = int(input("What is your number?"))
factorial = 1
product = 1

while factorial <= num:
    product = product * factorial
    factorial = factorial + 1
print(product)

#Exercise:
#Use the while loops to find the smallest number that is divisible by all integers from 1 to 9.
#answer:2520
