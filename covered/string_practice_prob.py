"""Program to add 'ing' at the end of a given string (length should be at least 3).
If the given string already ends with 'ing' then add 'ly' instead.
If the string length of the given string is less than 3, leave it unchanged."""
# str1 = input("Enter the string : ")

# if len(str1) >= 3:
#     if not str1.endswith('ing'):
#         str1 += 'ing'
#     else:
#         str1 += 'ly'
#     # str1 += 'ly' if str1.endswith('ing') else 'ing' # above if else can also be written as
#     print('new string : ', str1)
# else:
#     print(str1)


# in one line
# str1 += 'ly' if str1.endswith('ing') else 'ing' if len(str1) >= 3 else ''
# print(str1)

"""Write a Python function to get a string made of its first three characters of a specified string.
 If the length of the string is less than 3 then return the original string. 
"""
# str4 = input("Enter a string : ")
# print(str4[:3] if len(str4) >=3 else str4)


"""Write a Python program to change a given string to a new string where 
the first and last chars have been exchanged."""
# str2 = input("enter a string : ")
# # string
# print(str2[-1] + str2[1:-1] + str2[0])


# string is immutable so we cannot change/modify its state
# s = "hello"
# print(s[3])
# s[3] = 'j'


""" Write a Python program that accepts a comma separated sequence of words as input and print as list 
"""
# str3 = input("Enter comma separated string : ")
# str3 = str3.split(',')
# print(str3)


'''print the below format 
*
* *
* * *
* * * *
'''

# for i in range(5):
#     print('* ' * i)





