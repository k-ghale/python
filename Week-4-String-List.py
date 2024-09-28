# # lab week 4
# # +++++++++++++++++++++++++++++++++++
# # https://peps.python.org/pep-0008/
# # https://docs.python.org/3/library/
# # https://www.w3schools.com/python/python_scope.asp
# # +++++++++++++++++++++++++++++++++++
# # STRING
# # +++++++++++++++++++++++++++++++++++
# # string data is one of the most common data types you will encounter in Python. 
# # String data is data consisting of an ordered sequence of characters
# print("This is a string message") 

# print("Starting line\nnew line added\n") 


# print('this ' \
#       'is ' \
#         '1 line') 

# print('''line 1
#       line 2
# line 3
#       line4''') 

# # An index is a number assigned to every element in a sequence that indicates its position. 
# # With strings, this means each character in the string has its own index. Indices start at 0. 
# # Example  
# print("abcdef"[0]) # a

# # You can also use negative numbers as indices. 
# # This is based on their position relative to the last character in the string. starting from -1
# print("abcdef"[-1]) # f

# # Bracket notation refers to the indices placed in square brackets. 
# # You can use bracket notation to extract a part of a string.
# # You can apply the same bracket notation to the variable:
# user_id = "abcdef"
# print(user_id[0]) # a

# # You can also take a slice from a string. 
# # When you take a slice from a string, you extract more than one character from it. 
# # The slice starts at the 0 index, but the second index specified after the colon is excluded. 
# print("abcdef"[0:3]) # abc


# # The str() function converts its input object into a string. 
# # Converting an integer to a string gives you the ability to search through it and extract slices from it.
# print(type(123)) # <class 'int'>
# print(type(str(123))) # <class 'str'>

# # len() function, which returns the number of elements in an object.
# print(len("abcdef")) # 6

# # You can also apply methods to strings, including the .upper(), .lower(), and .index() methods. 
# # A method is a function that belongs to a specific data type.
 a = 'the quick brown fox jumps over the lazy dog'
 print(a.split())
 print(a.upper())
 print(a.lower())
 print(a.capitalize())
 print(a.title())
# print(a.replace('o', '0'))
# print(a.replace('o', 'O').swapcase())
# print(a.find('dog'))

# # The .index() method finds the first occurrence of the input in a string and returns its location. 
# print("abcdef".index("a")) # 0 
# print("abcdef".index("d")) # 3
# # print("abcdef".index("m")) # ValueError: substring not found

# # The .index() method can also be used to find the index of the first occurrence of a substring. 
# tshah_index = "tsnow, tshah, bmoreno - updated".index("tshah")
# print(tshah_index) # 
# # The .index() method returns the index 7, which is where the substring "tshah" starts.

# # Strings are immutable.
# name = 'john'
# print(name[1])
# # name[1] = 'O' # TypeError: 'str' object does not support item assignment
# # 'john'[1] = 'O' # TypeError: 'str' object does not support item assignment

# college_name = "Centennial"
# campus_name = "Progress"
# full_detail = f"The college name is: {college_name} {campus_name}"
# print(full_detail)

# # +++++++++++++++++++++++++++++++++++
# # LIST
# # +++++++++++++++++++++++++++++++++++
# # List data is a data structure that consists of a collection of data in sequential form. 
# # You can use lists to store multiple elements in a single variable. 
# # A single list can contain multiple data types. 

# # Like strings, you can work with lists through their indices, and indices start at 0. 
# # In a list, an index is assigned to every element in the list.

# # Similar to strings, you can use bracket notation to extract elements or slices in a list.
# # To extract an element from a list, after the list or the variable that contains a list, add square brackets that contain the index of the element.

# list = ["abc", "def", "ghi", True, 12345]
# print(list[2])
# # OR 
# print(["abc", "def", "ghi", True, 12345][2])
# # negative index
# print(list[-3])

# # Extracting a slice from a list
# print(list[1:3])

# # Unlike strings, you can also use bracket notation to change elements in a list. 
# # This is because a string is immutable and cannot be changed after it is created and assigned a value, 
# # but lists are not immutable.
# list = ["abc", "def", "ghi", True, 12345]
# print("Before changing an element:", list)
# list[1] = "newElement"
# print("After changing an element:", list)

# # The .append() method adds input to the end of a list. 
# # Its one parameter is the element you want to add to the end of the list. 
# list = ["abc", "def", "ghi", True, 12345]
# print("Before appending an element:", list)
# list.append("mno")
# print("After appending an element:", list)

# # The .insert() method adds an element in a specific position inside a list. 
# # It has two parameters. The first is the index where you will insert the new element,
# #  and the second is the element you want to insert.
# list = ["abc", "def", "ghi", True, 12345]
# print("Before inserting an element:", list)
# list.insert(2,"element02")
# print("After inserting an element:", list)

# # The .remove() method removes the first occurrence of a specific element in a list. 
# # It has only one parameter, the element you want to remove.
# # Note: If there are two of the same element in a list, 
# # the .remove() method only removes the first instance of that element and not all occurrences.
# list = ["abc", "def", "ghi", True, 12345]
# print("Before removing an element:", list)
# list.remove("ghi")
# print("After removing an element:", list)

# list = ["abc", "def", "ghi", True, 12345]
# print("Before pop an element:", list)
# list.pop(2)
# print("After pop an element:", list)

# list = ["abc", "def", "ghi", True, 12345]
# print("Before del an element:", list)
# del list[2]
# print("After del an element:", list)

# list = ["abc", "def", "ghi", True, 12345]
# print("Before del the list:", list)
# del list
# print("After del the list:", list)

# # Similar to the .index() method used for strings, 
# # the .index() method used for lists finds the first occurrence of an element in a list and returns its index. 
# # It takes the element you're searching for as an input.
# # Note: Although it has the same name and use as the .index() method used for strings, 
# # the .index() method used for lists is not the same method. 
# # Methods are defined when defining a data type, and because strings and lists are defined differently, 
# # the methods are also different.
# list = ["abc", "def", "ghi", True, 12345]
# element_index = list.index("ghi")
# print(element_index)

# # https://www.w3schools.com/python/python_lists_methods.asp
