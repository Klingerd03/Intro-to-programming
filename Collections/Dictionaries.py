# dict1 = {"num1": "Donald", "num2": "Mickey"}
# dict2 = {1:123, 2:234, 3:345, "a":123}
# print(dict1)
#
# print(dict1["num1"])
# print(dict1["num2"])
# print(dict2[3])
#
# length_of_dictionary = len(dict1)
#
# class_roster = {101:'jay', 102:'andy', 103:'robert', 104:'emma'}
# roll_1 = class_roster[101]
# print(roll_1)
#
#
# dict_of_squares = {}
# for i in range(10):  #gives you 0-9 elements
#     dict_of_squares[i] = i**2   #**2 is the square of i
# print(dict_of_squares)
#
# print(len(dict_of_squares))
# del (dict_of_squares[5])
# print(dict_of_squares)


#Exercise:
#Create a dictionary of numbers and their cubes between 1 to 100 that are divisible by 5

# dict_of_num = {}
# for i in range (1,101):
#     if i%5 == 0:
#         dict_of_num[i] = i**3
# print(dict_of_num)

#rewrite this using a while loop:
# num = 1
# dict_of_num = {}
#
# while num <=100:
#     if num%5 == 0:
#         dict_of_num[num] = num**3
#     num += 1
# print(dict_of_num)



#Methods of Dictionary
#items
#keys
#copy
#values

# dict1 = {1:"Donald", 2:"Mickey", 3:"Bugs", 4:"Daffy", "five":"SpongeBob"}
# print(dict1)
# print(type(dict1))
# #a class has a bunch of methods which manipulate the data in the class
#
# #use the keys method to get all the keys in the dictionary
# print(dict1.keys())
#
# #use the values method to get all the values in the dictionary
# print(dict1.values())
#
# #use the keys method to iterate through all the keys in the dictionary
# for k in dict1.keys():
#     print (k)
#
# for k in dict1.keys():
#     print(k)
#     print(dict1[k])
#
# #use the keys method to iterate through each key in the dictionary and then use its
# # value
# for k in dict1.keys():
#     if (dict1[k] == "Bugs"):
#         print("Value Bugs has key:", k)
#
# #use the value method to iterate through each value in the dictionary
# print(dict1.values())
# for val in dict1.values():
#     print(val)
#
# #items method outputs the key:value pairs are tuples
# print(list(dict1.items()))
#
# dict2 = {"narendra":123, "john":"hall", 45:376, "gate":345.76}




#Exercise:
#Use a long string. Find the number of times each word occurs in that string.
#Journyx technology, from the source code of our software to the code that maintains our Web site and ASP sites, is entirely based on Python. It increases our speed of development and keeps us several steps ahead of competitors while remaining easy to read and use. It's as high level of a language as you can have without running into functionality problems. I estimate that Python makes our coders 10 times more productive than Java programmers, and 100 times more than C programmers.
#start by turning string into a list, access first element of the list. list method
# count to see if that element occurs in the list and create a dictionary of those.

str1 = "Journyx technology, from the source code of our software to the code that maintains our Web site and ASP sites, is entirely based on Python. It increases our speed of development and keeps us several steps ahead of competitors while remaining easy to read and use. It's as high level of a language as you can have without running into functionality problems. I estimate that Python makes our coders 10 times more productive than Java programmers, and 100 times more than C programmers."

list1 = str1.split()
print(list1[0])
print(list1)

dict3 = {}

for element in list1:
    if element not in dict3.keys():
        dict3[element] = list1.count(element)
print(dict3)

#another way to do the same problem:

letter_count = {}

for char in str1:
    if char in letter_count.keys():
        letter_count[char] += 1
    else:
        letter_count[char] = 1
print(letter_count)
#this will give you each letter individually, the difference between using the split
# and not using the split. Using the split will give you each word. This is giving
# you the count of each letter. It also gives upper case and lower case different
# counts. One is counting words and one is counting alphabets.