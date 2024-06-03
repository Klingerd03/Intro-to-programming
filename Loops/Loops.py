#For Loop

# wizard_players = ['Trevor', 'Bradley', 'Troy', 'Thomas', 'Randy']
#
# for player in wizard_players:
#     print("player name =", player)
#     print("this player is good")


# list1 = [1,2,3,4,5,6,7,8,9,10, 11, 12, 13]
# sum = 0
# for i in list1:
#     sum = sum + i
#
# print(sum)


# list1 = [1,2,3,4,5,6,7,8,9,10, 11, 12, 13]
# sum = 0
# for num in list1:
#     if num%2 == 0:   #if it is an even number from the list
#         sum = sum + num  #if even, add them
# print(sum)    #will give the even numbers from the list
#

# if(sum %2 == 0):
#     print(sum)
#     sum = sum ** 2



#Example
# list1 = [1, 4, 2, 7, 8, 12]
# for num in list1:
#     print(num ** 0.5)


# list1 = [1, 4, 2, 7, 8, 12]
# for num in list1:
#     if num % 2 == 0:
#         print(num)

# list1 = [1, 4, 2, 7, 8, 12]
# count = 0
# for num in list1:
#     if num % 2 == 0:
#         count = count + 1
#         print(count)


# count the number of words of length of 5 in the following paragraph:
# “Understanding that hard problems can be solved by step-by-step algorithmic processes (and having technology to execute these algorithms for us) is one of the major breakthroughs that has had enormous benefits. So while the execution of the algorithm may be boring and may require no intelligence, algorithmic or computational thinking — i.e. using algorithms and automation as the basis for approaching problems — is rapidly transforming our society. Some claim that this shift towards algorithmic thinking and processes is going to have even more impact on our society than the invention of the printing press. And the process of designing algorithms is interesting, intellectually challenging, and a central part of what we call programming.”

str1 = "Understanding that hard problems can be solved by step-by-step algorithmic processes (and having technology to execute these algorithms for us) is one of the major breakthroughs that has had enormous benefits. So while the execution of the algorithm may be boring and may require no intelligence, algorithmic or computational thinking — i.e. using algorithms and automation as the basis for approaching problems — is rapidly transforming our society. Some claim that this shift towards algorithmic thinking and processes is going to have even more impact on our society than the invention of the printing press. And the process of designing algorithms is interesting, intellectually challenging, and a central part of what we call programming."
list1 = str1.split()
count = 0
for word in list1:
    if len(word) == 5:
        count = count + 1
print(count)
