#Fibonacci Series
# a=1
# b=1
# count = 2
# fib = [a,b]
# print("first term = ", a)
# print("second term = ", b)
#
# sum = 0
# while count <= 100:
#     next_term = a+b
#     fib.append(next_term)
#     a=b   #this and the next line are the swap
#     b=next_term #this is part of the swap
#     #a,b = b, next_term
#     count +=1
# print(fib)


#Using the break statement
# a=1
# b=1
# count = 2
# fib = [a,b]
# while True:
#     next_term = a+b
#     print(count, "th term = ", next_term)
#     a,b = b, next_term  #this step is the same as the swap from the previous code chunk.
#     count += 1  #short form of count = count + 1
#     fib.append(next_term)
#     if (count ==10):
#         break
# print(fib)


#Exercise:
#Find the sum of the first 100 terms of the Fibonacci series. Start w/ a=1, b=1.

# a=1
# b=1
# fib = [a,b]
# count = 2
# sum = a+b
#
# while count < 5:
#     next_term = a+b
#     fib.append(next_term)
#     a=b   #this and the next line are the swap
#     b=next_term #this is part of the swap
#     count +=1
#     sum = sum + next_term
#     print(sum)
# print(fib)


#Exercise:
#you need the first term and the difference to find all the other terms of the series.
#First term a1= 1
#Difference d=3
#nth term a_n = a1 + (n-1)*d    n is the term number
#Use the while loop to find first 10 terms, n is the number of terms
#answer: [1, 4, 7, 10, 13, 16, 19, 22, 25]

# a1 = 1
# d = 3
# n=1
# terms = []
#
# while n<10:
#     a_n = a1 + (n - 1) * d
#     terms.append(a_n)
#     n+=1
# print(terms)


#Exercise: Triangular numbers
#T1 = 1
#Nth triangular number Tn = ( n*(n+1))/2
#Second triangular number T2 = 2*(2+1)/2 = 2*3/2 = 3
#Third triangular number T3 = 3(3+1)/2 = 3*4/2 = 6
#Write a while loop to find the first 10 triangular numbers

# T1 = 1
# n=1
# terms = []
#
# while n<=10:
#     Tn = (n*(n+1))/2
#     terms.append(Tn)
#     n+=1
# print(terms)


#Exercise: Fibonacci series using For Loop:
#Use the for loop to generate the first 100 Fibonacci series terms

# a=1
# b=1
# fib = [a,b]
#
# for i in range (100):
#     next_term = a+b
#     fib.append(next_term)
#     a=b   #this and the next line are the swap
#     b=next_term #this is part of the swap
# print(fib)



#Exercise: Geometric Series:
#a1=2
#Ratio r = 2
#Nth term an=a1*(r**(n-1))
#Geometric Series = [2,4,8,16,32,64,128...]
#Find the first 10 terms of this series.

# a1 = 2
# r = 2
# n=1
# Geometric_series = []
#
# while n<=10:
#     an=a1*(r**(n-1))
#     Geometric_series.append(an)
#     n+=1
# print(Geometric_series)



#Exercise:
#Find the first term in the series greater than 10000, use while true format.

a=1
b=1
fib = [a,b]
count = 0

while True:
    next_term = a+b
    if (next_term >10000):  #moving this if statement to the top of the loop makes it
        # so that anything over 10,000 won't be already added to the list. It will
        # check the count before performing the loop.
        print(next_term, count)
        break
    print(count, "th term = ", next_term)
    fib.append(next_term)
    a=b   #this and the next line are the swap
    b=next_term #this is part of the swap
    count += 1
print(fib)
print(len(fib))



