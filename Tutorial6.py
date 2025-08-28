# Functions & Recursions ------------------------------------------------------------------------------>

# Functions -------------------------------------->

def sum(a, b) :
    sum = a + b
    return sum
print("Sum = ", sum(3, 2))

print("Sum = ", sum(10, 12))
print("-------------------------------------------------------------------------------")
# Functions reduces the code length and makes it more readable. Decrease the redundency of code.

def mult(a, b) :
    mult = a * b
    return mult
print("Mult = ", mult(6, 7))
print("-------------------------------------------------------------------------------")

# Calculate the avg of 3 numbers ---->
def calAvg(a, b, c) :
    avg = (a + b + c) / 3
    return avg
print("Average is = ", calAvg(2, 6, 9))
print("-------------------------------------------------------------------------------")

# Default Parameter ----->
def calSum (a = 2, b = 5) :
    sum = a + b
    return sum
print("Sum is = ", calSum())
print("-------------------------------------------------------------------------------")

# WAF to print the length of a list ----->
def printListLength(lst) :
    return len(list1)

list1 = ["Anish","Kitty","Fultushi"]
print("The length is = ", printListLength(list1))
print("-------------------------------------------------------------------------------")

# WAF to print the elements of a list in same line ---->
def printListElements(list2) :
    for i in list2:
        print(i, end = " ")

list2 = ["Anish","Kitty","Fultushi"]
printListElements(list2)
print("\n-------------------------------------------------------------------------------")

# WAF to find a factorial of n ---->
def factorial(n) :
    fact = 1
    for i in range(n, 1, -1) :
        fact = fact * i
    return fact
print("The Factorial of 5 is = ", factorial(5))
print("-------------------------------------------------------------------------------")

# WAF to convert USD to INR ---->
def usdTOinr(n) :
    inr = n * 80
    return inr
print("4 USD = ", usdTOinr(4), "Rs")
print("-------------------------------------------------------------------------------")

# WAF to check whether a number is even or odd ---->
def checkEvenOdd(n) :
    if n % 2 == 0 :
        print(n,"is Even")
    else :
        print(n,"is Odd")
checkEvenOdd(5)
checkEvenOdd(10)
print("-------------------------------------------------------------------------------")

# Recursion -------------------------------------------------------------------------------------------------->

def show(n) :                   # Recursive Function
    if (n == 0) :               # base case
        return
    print(n)
    show(n-1)
show(5)
print("-------------------------------------------------------------------------------")

# WAF to find a factorial of any number n using Recursion ---->
def facto(n) :
    if(n == 0) :
        return 1
    return n * facto(n-1)
print(facto(5))
print("-------------------------------------------------------------------------------")

# WAF to calculate the sum of first n natural numbers using Recursion ---->
def calculateSum(n) : 
    if(n == 1) : 
        return 1
    return n + calculateSum(n-1)
print(calculateSum(10))
print("-------------------------------------------------------------------------------")