# fruits = ["apple", "orange", "banana", "kiwi", "mango"]
# print(fruits)
#
# print(fruits[1])
# print(fruits[-2])
# print(fruits[4])


numbers = [23, 45, 12, 67, 89, 100, 2, 5, -5]
# print(numbers[4] + numbers[5])
# print(numbers[3]*numbers[-2])

#slicing a list
# print(numbers[3:5])
# print(numbers[0:7])
# print(numbers[2:8])
# print(numbers[:3])
# print(numbers[1:3])
# print(numbers[3:5])
# print(numbers[2:6])
# print(numbers[7])
# print(numbers[-3:-1])
# print(numbers[5:])
# print(numbers[:5])
# print(numbers[-3:])
# print(numbers[::-1]) #reverse order
# print(numbers[0:99]) #will give you entire list
# ###print(numbers[99]) #will give an error that it's out of range of list.
# print(numbers[::1])


#To obtain the length of the list
# lengthoflist = len(numbers)
# ##or
# print(len(numbers))

#To delete an element of the list
# del(numbers[3])
# print(numbers)


#To use the "in" function and "not in" function
# squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
# var2 = 5
# if var2 in squares:
#     print ("5 is in the list")
#
# if var2 not in squares:
#     print ("var2 not in squares")

#example:
# even = [3, 7, 5, 13, 17, 21, 23, 33, 27, 19]
# print(len(even))
# del(even[5])
# print(even)
# var1 = 6
# if var1 in even:
#     print("6 is in the list")
# var2 = 7
# if var2 in even:
#     print("7 is in the list")
# var3 = 21
# if var3 not in even:
#     print("21 is not in the list")



# list1 = [1,3,5,7,9,11]
# list1.append("Klinger")
# print(list1)
# print(type(list1))
# list1.remove("Klinger")
# print(list1)
# list1.insert(2,231)
# print(list1)
# print(max(list1))



#Exercise
# even = [2,4,6,8,10,12,14,16,18,20]
# even.append(22)
# print(even)
# even.insert(10,21)
# print(even)
# print(even[::-1])
# #missing this line
# print(len(even))
# #missing this line - clear the list



str1 = "This is American University. It is a great place to study"
#print(str1[3:9])
#list1 = str1.split()
#print(list1)
# list1 = str1.split(".")
# print(list1)


#Lists within a list (nested)
# matrix1 = [ [1,2,3], [3,9,81], [4,16,64] ]
# print(matrix1[1][1])
