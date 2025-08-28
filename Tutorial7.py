# File I/O ---------------------------------------------------------------------------------------------->

# Text Files ----> .txt, .docx, .log
# Binary Files ----> .jpg, .png, .mp3, .mp4,

# File Opening ---->
f = open("demo.txt", "r")               # Read mode ( Default mode )
data = f.read()
print(data)
print(type(data))
f.close()
print("------------------------------------------------------------------------------")

f1 = open("demo.txt","r")
data1 = f1.read(7)
print(data1)
f1.close()
print("------------------------------------------------------------------------------")

f2 = open("demo.txt","r")
line1 = f2.readline()                   # Line by line reading
print(line1)
f2.close()
print("------------------------------------------------------------------------------")

# If we read a file before using readline(), then it will print empty space.

f3 = open("demo.txt","w")               # Overwrite the file. File Writing
f3.write("Hello, I am a beginner in Python programming.")
f3.close()
print("------------------------------------------------------------------------------")

f4 = open("demo.txt","a")               # Append the file
f4.write("\nI am learning Python from Apna College")
f4.close()
print("------------------------------------------------------------------------------")

f5 = open("demo.txt","r+")              # For reading & writing
f5.write("Hi I am Anish,")              # It will first overwrite the file according to a pointer
print(f5.read())
f5.close()
print("------------------------------------------------------------------------------")

f6 = open("demo.txt","w+")              # Truncate the file
print(f6.read())
f6.write("<----- Anish ----->")
f6.close()
print("------------------------------------------------------------------------------")

f7 = open("demo.txt","a+")              # Append the new statements in the file
f7.write("<----- Shrestha ----->")
f7.close()
print("------------------------------------------------------------------------------")

# Another way to open a File ----->
with open("demo.txt","r") as f :        # It will automatically close the file after operations
    data = f.read()
    print(data)

with open("demo.txt","w") as f :
    f.write("<----- Anish & Shrestha ----->")

# Deleting a File ---->

import os                           # Built in Module
# os.remove("sample.txt")

# Practice -------------------------------------------------------------------------------------------------->
# Create a file practice.txt using python and add some lines and then delete it.

with open("practice.txt","w") as f :
    f.write("Hi Everyone\nWe are learning File I/O in Python\n")
    f.write("I like programming")

# os.remove("practice.txt")