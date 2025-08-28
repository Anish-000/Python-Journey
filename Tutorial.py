print("Hello World")
print ("Anish Chattopadhyay")

print ("Hello World","I am Anish")
print("Age is : ",21)

print ("Sum : ", 67 + 22)

# variables and Data Types ------------------------------------------------------------>

name = "Anish"
print(name)

age = 21
print(age)

print ("My name is ", name, " and I am " , age , " years old ")

# finding types of variables ------------------------------------------------------------>

print(type(name))
print(type(age))

old = False
print(old)

a = None
print(a)

print(type(a))
print(type(old))

# arithmetic operations of two numbers -------------------------------------------------------------->

a = 10
b = 7
sum = a + b
print("Sum (a + b) : ", sum)

sub = a - b
print ("Sub (a - b) : ", sub )

mult = a * b
print("Mult (a * b) : ", mult)

div = a / b
print("Div (a / b) : ", div)

mod = a % b
print("Mod (a % b) : ", mod)

pow = a ** b
print("Power (a ** b) : ", pow)

# Comparison Opertaors ------------------------------------------------------------------------->

print ( a == b)  # False
print ( a != b)  # True
print ( a > b)  # True
print ( a < b)  # False
print (a >= b)  # True
print (a <= b)  # False

# Assignment Operators -------------------------------------------------------------------------->

num = 10
print("Num : ", num)

num1 = 20
num1 += num
print ("Num1 : ", num1)

# Type Conversion and Type Casting ----------------------------------------------------------------->

x = 2
y = 4.56

add = x + y
print("Sum (x + y) : ", add)  # Type Conversion

z = "3"
p = float(z)

add = p + x
print("Sum (p + x) : ", add)  # Type Casting

# Input from Keyboard ------------------------------------------------------------------------->

name = input("\nEnter you name : ")
age = int(input("\nEnter Age : "))
marks = float(input("\nEnter marks : "))

print("Hello, ", name)
print("Your Age is : ", age)
print("You have got ", marks, "%")

print("\n")
FirstNum = int(input("Enter First Number : "))
SecondNum = int(input("Enter Second Number : "))

print ("Sum = ", FirstNum + SecondNum)