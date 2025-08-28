# List & Tuples --------------------------------------------------------------------------------------->

# Lists ------------->
marks = [94.4, 88.5, 76.7, 92.1, 85.6]
print(marks)
print(type(marks))

print(marks[0])
print(marks[3])

print(len(marks))

# Lists can contain different data types. Example ---->
student = ["Anish", 95.4, 21, "Chakdaha"]
print(student)

# Lists are mutable but strings are not. Example ----->
str = "Hello"
print(str[0])
# str[0] = "y"        # it is not allowed in pyhton

student[0] = "Shrestha"
print(student)

# List slicing --------------------------------------------------------------------->

print(student[1:3])
print(student[0:3])
print(student[0:4])

print(student[-3:-1])       # Negative indexing

# Lists Methods -------------------------------------------------------------------->

list = [1,2,4]
print(list)
list.append(3)      # append() method is used to add an element at the end of the list
print(list)

list.sort()         # sort() method is used to sort the list in ascending order
print(list)

list.sort( reverse = True )     # sort() method is used to sort the list in descending order
print(list)

list1 = ["Banana", "Litchi", "Apple"]
list1.sort()
print(list1)

list1.sort( reverse = True )
print(list1)

list2 = ["Baloon", "Banana", "Bar"]
list2.sort()
print(list2)

list2.sort( reverse = True )
print(list2)

list4 = ["a", "b", "c", "d", "e"]
list4.reverse()                             # reverse() method is used to reverse the list
print(list4)

list4.insert(3,"f")             # insert() method is used to insert an element at the specified position
print(list4)

list4.pop(3)                    # pop() method is used to remove an element at the specified position
print(list4)

list4.remove( "a" )             # remove() method is used to remove the first occurrence of the specified element
print(list4)

# Tuples ---------------------------------------------------------------------------------------------------------->

tuple = (2, 1, 4, 3)
print(type(tuple))

print(tuple[2])
print(tuple[3])

# tuple[0] = 5            # it is not allowed in python because tuples are immutable

tuple1 = ()
print(tuple1)

# Difference between creating a tuple with single element

tuple2 = (1,)               # It is the right way to create a tupple. Why comma ? lets see...
print(tuple2)
print(type(tuple2))

tuple3 = (1)
print(tuple3)
print(type(tuple3))         # The difference is comma.

# Tuple slicing -------->

print(tuple[1:3])
print(tuple[:3])
print(tuple[1:])

# Tuple Methods ----------->

print(tuple.index(4))       # index method returns the index of the first occurrence of the specified element

tuple4 = (1, 2, 1, 4, 1)
print(tuple4.count(1))     # count method returns the number of occurrences of the specified element

# Practice -------------------------------------------------------------------------------------------------------->

# 1. WAP to ask the user to enter names of their 3 fav movies & store them in a list

list5 = []
str1 = input("\nEnter your first fav movie name: ")
str2 = input("\nEnter your second fav movie name: ")
str3 = input("\nEnter your third fav movie name: ")

list5.append(str1)
list5.append(str2)
list5.append(str3)

print("\n",list5)

# 2. WAP to check if a list contains a palindrome of elements.

list6 = [1, 2, 3, 2, 1]

list7 = list6.copy()
list7.reverse()

if(list7 == list6):
    print("\n",list6,"is a palindrome")

# 3. WAP to count the number of students with the "A" grade in the following tuple
# ('A', 'B', 'A', 'A', 'B', 'A')

tup = ("A", "B", "A", "A", "B", "A")
count = tup.count("A")
print("\nNumber of students with grade A:", count)

# Store the above values in a list and sort them

list8 = ["A", "B", "A", "A", "B", "A"]
list8.sort()
print(list8)