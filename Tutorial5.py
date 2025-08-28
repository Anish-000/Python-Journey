# Loops & Functions ----------------------------------------------------------------------------------------------->

# While Loop --------------->

# while True :                            # Run for infinite time
#     print("Hello, World!")

count = 1                               # Run for 5 times
while count <= 5 : 
    print("Hello")
    count += 1
print(count)                            # Print the value of count
print("----------------------------------------")

i = 1
while i <= 3 :
    print("Anish", i)
    i += 1
print("----------------------------------------------")

# Print numbers from 1 to 5 -------------->
j = 1
while j <= 5 : 
    print(j)
    j += 1
print("---------------------------------------------")

# Print numbers from 5 to 1 -------------->
k = 5
while k >= 1 :
    print(k)
    k -= 1
print("--------------------------------------------------")

# 1. Print the multiplication table of a number n
num = 3                                         # You can take user input as well
i = 1
while i <= 10 :
    print(i,".", 3*i)
    i += 1
print("--------------------------------------------------")

# 2. Print the elements of the following list using a while loop
#     [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
num1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
i = 0
while i < len(num1) :
    print(num1[i])
    i += 1
print("--------------------------------------------------")

# Search for a number x in a tuple
#     (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

num2 = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 36
i = 0
while i < len(num2) :
    if (num2[i] == x) :
        print("Found ",x,"at index", i)
    else :
        print("Finding...")
    i += 1
print("--------------------------------------------------")

# Using break & continue statements -------------------------------------------------->
# Break ------------------------------------------------->

num3 = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 36
i = 0
while i < len(num3) :
    if (num2[i] == x) :
        print("Found ",x,"at index", i)
        break
    else :
        print("Finding...")
    i += 1
print("End of Loop")
print("--------------------------------------------------")

# Continue ----------------------------------------------->

m = 0
while m <= 4 :
    if (m == 2) :
        m += 1
        continue            # It will skip the print statement and m += 1 below
    print(m)
    m += 1
print("--------------------------------------------------")

# For Loop ---------------------------->

list1 = [1, 2, 3, 4, 5]
for i in list1 :
    print(i)
print("--------------------------------------------------")

tup1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for i in tup1 :
    print(i)
print("--------------------------------------------------")

# 1. Print the elements of the following list using for Loop
# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

list2 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for i in list2 :
    print(i)
print("--------------------------------------------------")

# Search for a number x in the following tuple using for loop 
# tup = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

tup2 = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 49
i = 0
for el in tup2 :
    if(el == x) : 
        print("Found ", x, "at index", i)
    i = i+1
print("--------------------------------------------------")

# Range Function -------------------------------------------------------------->

seq = range(5)          # Alternative way --> for i in range(5) : print(i)
for i in seq :          # range(stop)
    print(i)
print("--------------------------------------------------")

for i in range(2,10) :      # range(start,stop)
    print(i)
print("--------------------------------------------------")

for i in range(2,10,2) :    # range(start,stop,step size)   Step size can be negative
    print(i)
print("--------------------------------------------------")

# Empty Loop ----->

for i in range(5) :
    pass

print("Anish")
print("--------------------------------------------------")

# WAP to find the sum of first n numbers.

sum = 0
n = 10
for i in range(n+1) :
    sum = sum + i
print(sum)
print("--------------------------------------------------")

# Factorial of any number

n = 5
mult = 1
for i in range(1,n+1) :
    mult *= i
print(mult)
print("--------------------------------------------------")