d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# check if key present in dict


"""Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form 
(x, x*x).
n = 5
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""
# n = int(input("Input a number "))
# d = dict()
#
# for x in range(1, n + 1):
#     d[x] = x * x
#
# print(d)
#
# print({x: x*x for x in range(1,6)})

"""sum all dict values"""
d1 = {'a': 100, 'b': -50, 'c': 240}
print(sum(d1.values()))
# print(d1.values())


"""multiply all value in dict"""
# d1 = {'a': 10, 'b': 5, 'c': 40}
# a = 1
# for i in d1.values():
#     a *= i
# print(a)

"""delete specific key from dict"""
# myDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# print(myDict)
# if 'a' in myDict:
#     del myDict['a']
# print(myDict)

"""sort a dict based on key"""
# color_dict = {'red': '#FF0000',
#               'green': '#008000',
#               'black': '#000000',
#               'white': '#FFFFFF'}
# print(sorted(color_dict))

"""check if dict empty or not"""
# a = {}
# if not a:
#     print("empty")
# else:
#     print('not empty')
# # print(bool(a))


# #  Use a dictionary comprehension to count the length of each word in a sentence
# words = "Hello I am testing a dict comprehension"
# r = {word: len(word) for word in words.split(" ")}
# print(r)

# # remove vowels using list comp from a string
# string = "Hello I am testing a dict comprehension"
# a = "".join([char for char in string if char not in ["a", "e", "i", "o", "u"]])
# print(a)


