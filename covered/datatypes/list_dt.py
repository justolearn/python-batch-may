# # Python program to demonstrate
# # Creation of List
#
# # Creating a List
# List = []
# l1 = list()
# print(l1)
# print("Intial blank List: ")
# print(type(List))
# print(List)
# print(type(List))
#
# # Creating a List with
# # the use of a String
# List = ['Python']
# print("List with the use of String: ")
# print(List)

# # Creating a List with
# # the use of multiple values
# List = ["Python", "Java", "C++"]
# print("List containing multiple values: ")
# print(List[0])
# print(List[2])
#
# # Creating a Multi-Dimensional List
# # (By Nesting a list inside a List)
List = [
    ['Java', 'Python'],
    ['C']
]
# print("Multi-Dimensional List: ")
# print(List)
# print(List[0])
# print(List[0][1])
# print(List[0][0])
# print(List[1])
# print(List[-1])
# print(List[-2][-1])


"""list operatoions"""
# # List concatenate
# a = [1,2,3,4]
# b = [5,6,3,4]
# print(a+b)

# # repetition
# a = [1,2,3]
# print(a*3)

# # reverse
# a = [1, 2, 3, 4]
# print(a[::-1])

# slicing
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a[::-1])

# print(len(a))
# print(a[-4::2])  # considering end as blank  6 to 9
# print(a[::2])  # display sliced list
# print(a[::3])  # display sliced list
# print(a[::-3])  # skip two element and print the third one last
# print(a[:5:-2])  # start from 5th index and slice from reverse


# # conversion
# a = (10, 20, 30)
# print(list(a))
# b = "hello"
# print(list(b))

# # membership for list element
# a = ["hello", 1, 45, "Bye"]
# print('hell' not in a)
# print('Bye' in a)
# print(1 in a)
# print(45 not in a)


# # loop through list
# list1 = ["apple", "banana", "cherry"]
# for x in list1:
#     print(x)
#
# for i in range(len(list1)):
#     print(list1[i])

#
#
# #  List comprehension

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)  # 'apple', 'banana', 'mango'
# print(newlist)
# #
# newlist = [x for x in fruits if "a" in x]
#
# print("lc : ", newlist)
# print("lc : ", *newlist)  # to print list element separated by space
# print(*newlist, sep=', ')  # to print list element separated by comma
# print(*newlist, sep='\n')  # to print list element separated by new line

# matrix
# matrix = [
#     [0, 1, 2, 3, 4],
#     [0, 1, 2, 3, 4],
#     [0, 1, 2, 3, 4]
# ]
# main_list = []
# for n in range(3):  # 0; 1; 2
#     inner_list = []
#     for i in range(5):  # 0 1 2 3 4
#         inner_list.append(i)  # 0,  1, 2, 3, 4
#
#     main_list.append(inner_list)  # [[0, 1,2 ,3,4], [0,...4], [0,...4]]
# print(main_list)

# a = [[j for j in range(5)] for i in range(3)]
# print(a)
# b = [num for num_list in a for num in num_list]
# print(b)

"""list method"""
# # # append(): Adds a single element to a list.
# a = [1,2,3,4,5,6,7]
# print('List  : ', a)
# a.append(8)
# print("appending in list : ",a)
# a.append([1,2,3])
# print(a)
# # print(a[-1][1])
# #
# # # remove specific item
# a.remove(8)
# print('removing from list',a)
# #
# # # remove from index
# a.pop(0)
# print('removing from list',a)
# a.pop()       # id no index specified will remove from last index
# print('removing from list',a)
# #
# # # delete also removes from specific
# del a[0]
# print('deleting from specific location ', a)
# #
# # # length of list
# print('length of list ', len(a))
#
# # count occurrence of element
# print(a.count(5))
# #
# # # clear
# a.clear()
# print(a)
# #
# # # delete entire list
# del a
# print(a)

# sorting alpha/numeric by default in asc
# fruitList = ["orange", "mango", "kiwi", "pineapple", "banana"]
# fruitList.sort()
# print(fruitList)
# fruitList.sort(reverse=True)    #descending order
# print(fruitList)
# a = [45, 21, 67, 1, 3]
# a.sort()
# print(a)

# # copy list
# fruitList = ["orange", "mango", "kiwi", "pineapple", "banana"]
# fruitList_1 = fruitList.copy()
# print('first list : ', fruitList)
# print(fruitList_1)


# # copy list using slicing
# fruitList = ["orange", "mango", "kiwi", "pineapple", "banana"]
# fruitList_1 = fruitList[:]
# print(fruitList_1)


# # join list
# # concatenate extend
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# list1.extend(list2)
# print(list1)

# # concatenate + operator
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# print(list1 + list2)

# # reverse list in place modification
# list2 = [1, 2, 3]
# print(list2.sort())
# print(list2)
# help(list.reverse)

# # insert at a specified pos
# list1 = [1, 2, 3, 4, 5]
# list1.insert(2, 8)
# print(list1)

# # join
# a = ['1','2','3','4']
# b = ''.join(a)
# print(b)

# # index return the first occurrence of specified value
# fruitList = ["orange", "banana", "kiwi", "orange", "banana"]
# print(fruitList.index('banana'))

# # max/ min
# numList = [1, 2, 8, 4, 5, 6, 7]
# print(max(numList))
# print(min(numList))

# # converting seq in list
# s = 'hello'
# print(list(s))
# t = (1, 2, 3, 4)
# print(list(t))


# # For which month price was min
# months = ['January', 'February', 'March']
# prices = [238.11, 237.81, 238.91]
# min_price = prices.index(min(prices))
# print("month with min price : ", months[min_price])
# print(max(months))
# print(min(months))
