# strings ------------------------------------------------------------------------------------------------>

str1 = "This is string1"
str2 = "This is string2"

str3 = str1 + " " + str2    # string concatination
print (str3)

str4 = "Anish"
str5 = "Chattopadhyay"

str6 = str4 + " " + str5
print (str6)

print(len(str5))            # string length

len1 = len(str1)
print(len1)

print(len(str6))

print(str1[0])              # string indexing
print(str1[4])
print(str6[7])

ch = str1[1 : 4]
print(ch)                   # string slicing
print(str4[1:3])
print(str5[0 : 6])

print(str5[0 : ])           # pyhton compiler assumes that we want to go till the end of the string

print(str5[-3 : -1])        # negative indexing
print(str5[-3 : ])

# string Functions ------------------------------------------------------------------------------------>

ch1 = "Anish Chattopadhyay"
print(ch1.endswith("ay"))

print(ch1.endswith("ya"))       # endswith always returns boolean value

ch2 = "anish"
print(ch2.capitalize())         # make the first letter capital

print(ch2.replace("n","s"))     # replace the old value with new one

ch3 = "I am learning Pyhton"
print(ch3.replace("Pyhton","JavaScript"))

print(ch2.find("i"))            # returns the position of the first occurrence of the specified value
print(ch2.find("a"))
print(ch3.find("learning"))
print(ch3.find("Q"))            # if the letter or word is not in the string it will return -1

print(ch3.count("a"))           # count the number of occurrences of the specified value
print(str5.count("y"))
print(ch3.count("am"))

# Practice ------------------------------------------------------------------------------------------------>

name = input("\nEnter your name : ")
print(name)
print(len(name))

ch4 = "$$ Anish Chattopadhyay $$"
print("Total occurance of $ is : ",ch4.count("$"))

# Conditional statement ------------------------------------------------------------------------------------->

# syntax -> if-elif-else

age = 16
if(age >= 18):
    print("You are eligible to vote")
else :
    print("You are not eligible to vote")

# max of 3 numbers 
num1 = 23
num2 = 45
num3 = 20

if((num1 > num2) & (num1 > num3)) :
    print(num1,"is the largest number")
elif((num2 > num1) & (num2 > num3)) :
    print(num2,"is the largest number")
else :
    print(num3,"is the largest number")

# Practice --------------------------------------------->

marks = int(input("\nEnter your Grade : "))
if(marks >= 90) :
    print("Grade A")
elif(marks >= 80) :
    print("Grade B")
elif(marks >= 70) :
    print("Grade C")
else :
    print("Grade D")

# nested if ---------------------------------------------------------->

driving_age = 61
if(driving_age >= 18):
    if(driving_age >= 60):
        print("You are not eligible to drive")
    else :
        print("You are eligible to drive")
else :
    print("You are not eligible to drive")

# Practice --------------------------------------------------------------------------->

num4 = int(input("\nEnter a Number : "))
if(num4 % 2 == 0):
    print(num4," is an even number")
else :
    print(num4," is an odd number")


num5 = int(input("\nEnter a Number : "))
if(num5 % 7 == 0):
    print(num5," is a multiple of 7")
else:
    print(num5," is not a multiple of 7")