var1 = 10
var2 =23
tolVar = var1 + var2
bvar = tolVar/var1

print(var1)
print(var2)
print(tolVar)
print(bvar)

#a because bvar is division and always results in floating output
#b
print(tolVar//var1)
#c
print(var2**7)
#d
print(tolVar**0.5)
print(9**0.5)

print(9**1/2)




# name = input("Enter your name here")
# print(name)
#
# major = input("Enter major here:")
# school = input("What school do you go to?")
# print(major)
# print(school)

# Var1 = input("Enter first number here:")
# print(type(Var1))
#
# newVar1 = int(Var1)
# print(type(newVar1))
#
# Var2 = input("Enter second number here:")
# newVar2 = int(Var2)
# print(type(newVar2))
#
# total = newVar1+newVar2
#
# print(total)

# Var1 = 10
# print(type(Var1))
# Var2 = 3.14
# print(type(Var2))
# Var3 = "Narendra"
# print(type(Var3))

# Var1 = input("Enter string1:")
# Var2 = input("Enter string2:")
#
# print(Var1+Var2)

#Simple Interest Exercise

P = int(input("Enter principal"))
N = int(input("Enter the period"))
R = float(input("Enter the rate of interest"))

A = P*N*R/100

print(A)