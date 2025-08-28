# Dictionary and Sets ---------------------------------------------------------------------------------------->

# Dictionary ------------------------------->
# A dictionary is a collection of key-value pairs. They are unordered and mutable and don't allow duplicate keys.

info = {
    "key" : "value",
    "name" : "Anish",
    "learning" : "Python",
    "age" : 21,
    "marks" : 90.5,
    "subjects" : ["C","C++","Pyhton"],
    "topic" : ("dict","sets")
}

print(info)
print(type(info))

print(info["age"])
print(info["subjects"])
print(info["learning"])

info["name"] = "Shrestha"       # Assinging New Value
print(info["name"])
print(info)

null_dict = {}                  # Null Dictionary
print(null_dict)

null_dict["name"] = "Anish"    # Assigning Value in Null Dictionary
print(null_dict)

# Nested Dictionary ----------------------------------------------------->

info1 = {
    "name" : "Anish",
    "age" : 21,
    "score" : {
        "phy" : 90,
        "chem" : 85,
        "math" : 95,
        "bio" : 92
    }
}

print(info1)
print(info1["score"])
print(info1["score"]["math"])

# Methods of Dictionary ----------------------------------------------------->

print(info1.keys())             # Returns all keys

print(len(info1))               # Returns the number of items in dictionary
print(len(info1["score"]))

print(info1.values())           # Returns all values
print(info1.items())            # Returns all key-value pairs

pairs = list(info1.items())
print(pairs)
print(pairs[0])

print(info1["name"])            # Returns the value of the key if it exists in dictionary
print(info1.get("name"))        # Returns the value for the given key if it exists in dictionary

# So what's the difference between print(info1["name"]) and print(info1.get("name"))?
# print(info1["name2"])          # Error
print(info1.get("name2"))        # Returns None value

info1.update({"City" : "Chakdaha"})
print(info1)

# Set in Python ------------------------------------------------------------------------------------------------>

# Set is the collection of unique elements which can be of any data type. It is mutable
# It is an unordered collection of unique elements.
# The elements of sets are immutable, i.e., it cannot be changed after creation.

collection = {1, 2, 3, 4}

print(collection)
print(type(collection))

coll = {1, 2, 3, "apple", "banana", 4, 2}       # Set can have duplicate values but it will be removed in output
print(coll)
print(len(coll))

# Empty set
coll1 = set()
print(coll1)
print(type(coll1))

# Methods of Set --------------------------------------------------------->

coll1.add(1)                        # Add an element to the set
coll1.add(2)
coll1.add(3)
coll1.add(3)

print(coll1)
coll1.add("Anish")
coll1.add("Shrestha")

print(coll1)

coll1.remove(3)                     # Remove an element from the set
coll1.remove("Anish")

print(coll1)

coll1.clear()                       # Clear the set
print(coll1)
print(len(coll1))

coll2 = {"Hello", "Anish", "I ", "am", "Python", "Programmer"}
print(coll2.pop())                  # Remove and return an element from the set (randomly)
print(coll2.pop())

coll3 = {1, 2, 3, 4, 5}
coll4 = {4, 5, 6, 7, 8}

print(coll3.union(coll4))           # Return a new set with elements from both sets
print(coll3.intersection(coll4))    # Return a new set with elements common to both sets

# Practice Questions ------------------------------------------------------------------------------>

# 1. Store the following word meanings in a python dictionary:
#   table : "a piece of furniture", "ists of facts and figures"
#   cat : "a small animal"

dict1 = {
    "table" : ["a piece of furniture", "ists of facts and figures"], 
    "cat" : "a small animal"
}

print(dict1)

# 2. You're given a list of subjects for students. Assume one classroom is required for 1 subject.
# How many classrooms are needed by all students
# "python","java","c++","c","javascript","python","c++","pyhton","c","java"

set1 = {"python","java","c++","c","javascript","python","c++","python","c","java"}
print(len(set1))