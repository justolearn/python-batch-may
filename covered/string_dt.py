
# String1 = 'Welcome to the Coding World'
# print("String with the use of Single Quotes: ")
# print(String1)
# print(type(String1))

# # Creating a String
# # with double Quotes
# String1 = "I'm a coder"
# print("String with the use of Double Quotes: ")
# print(String1)
# print(type(String1))
#
# # Creating a String
# # with triple Quotes
# String1 = '''I'm a coder and I live in a world of "coding"'''
# print("String with the use of Triple Quotes: ")
# print(String1)
# print(type(String1))
#
# # Creating String with triple
# # Quotes allows multiple lines
# String1 = '''coders
# For
# Life'''
# print("Creating a multiline String: ")
# print(String1)
# string_2 = "Hello  my name is Jhon and I am learning python because python is very intresting language. " \
#            "It has lot of features and very exciting set of libraries."
#
# multiline
# a = '1\
# 2\
# 3'
# print(a)
# a = '12' \
#     '3'
# print(a)
#
# # escape sequence
# print('\'You must be the change you\'r wish to see in the world\' - Gandhi')
#


"""string operator"""
#
# ''' operations on string'''
# 1. concat
# a = "Hello "
# b = "world"
# print(a+b)

#
#
#
# # 2. repetition
# print("Hi! "*10)

# Check existence of a character or a sub-string in a string
# print("won" in "India won the match")
# print("won" not in "India won the match")
#
#
#
#
# # 3. converting type
# a = '123'
# a_list = list(a)
# print('List : ', a_list)
# print('type of a_list : ', type(a_list))





# 4. slicing    (start:stop:step)
# slicing_ex0 = "My Name is Jhon"
# print('Slice From start : ', slicing_ex0[:7])
# slicing_ex1 = "My Name is Jhon"
# print('Slice to the end : ', slicing_ex1[3:])
# slicing_ex2 = "Hello Python"
# print(slicing_ex2[1:10])
# slicing_ex3 = "Hello World"
# print(slicing_ex3[0:10:2])
# slicing_ex4 = "0123456789"
# print(slicing_ex4[0:10:2])
# slicing_ex4 = "0123456789"
# print(slicing_ex4[::-1])
# slicing_ex5 = "Hello Python"
# print(slicing_ex5[-10:-1])



#
# # 5.reverse
# slicing_ex = "Hello Python"
# print(slicing_ex[::-1])

#
# str1 = "Hello Python"
# for i in str1:
#     print(i)


"""String method"""
# # 1. length
# str1 = "Check the length"
# print(len(str1))
#
# # 2. upper/lower
# str_ex = "all in lower"
# print("Text with lower case : ", str_ex)
# print("applying upper function : ",str_ex.upper())
# str_ex0 = "ALL IN UPPER"
# print("Text with upper case : ", str_ex0)
# print("applying lower function : ",str_ex0.lower())
#
#
# # 3. strip() method removes any whitespace from the beginning or the end:
# str_ex1 = "    hello world    "
# print("Text with white spaces : ", str_ex1)
# print("Text with strip function : ", str_ex1.strip())
#
# 4. Replace
# str_ex2 = "Hello, World!"
# print(str_ex2.replace("H", "J"))
#
# 5. split : Splits the string at the specified separator, and returns a list
# str_ex3 = "Hell on, World!"
# print(str_ex3)
# print(str_ex3.split(","))
#
# # 6. Formatting String
# x = 5
# y=10
# print('The value of x is {} and y is {}'.format(x,y))
# print('I love {0} and {1}'.format('bread','butter'))
# print('I love {1} and {0}'.format('bread','butter'))
# print('Hello {greeting}, {name}'.format(greeting = 'Goodmorning', name = 'John'))
# name = 'Mia'
# age = 10
# print(f'My Name is {name} & I am {age}')

# #  7. startswith / endswith
# str_ex4 = "BombayGoa"
# print('starts with example : ', str_ex4.startswith('Bom'))
# str_ex4 = "BombayGoa"
# print('ends with example : ', str_ex4.endswith('Goa'))

# join returns a string in which the elements of sequence have been joined by str separator.
# string1 = "hello"
# a = '-'.join(string1)
# print(a)



# a = "Hello python"
# print(a)
# print(a.replace('H', 'J'))
# print(id(a))
# a = "hii"
# print(id(a))
