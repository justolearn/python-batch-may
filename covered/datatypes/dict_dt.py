"""Blank dict"""
# d = {}
# print(type(d))
# d = dict()
# print(type(d))


"""accessing dict key value pair"""
# user = {'name': "Jhon", 'age': 28, "Country": "India"}
# print(user['name'])
# print(user['age'])
# print(user.get('name'))

"""adding and updating dict value"""
user = {'name': "Jhon", 'age': 28, "Country": "India"}
# # add item
# user['phone_number'] = "55555555"
# print(user)
# # update item
# user['phone_number'] = "66666666"
# print(user)
# # update item
user.update({'Country': ["India", "US", "UK"]})
print(user)
print(user['Country'][1])
user.update({'pin': 4532})
print(user)

"""get keys"""
# user = {'name': "Jhon", 'age': 28, "Country": "India", "phone_number": 123456789}
# print(user.keys())


"""remove element from dict"""
# user = {'name': "Jhon", 'age': 28, "Country": "India", "phone_number": 123456789}
# user.pop('phone_number')
# print(user)
# # user.clear()
# # print(user)
# # del user['age']
# # print(user)
# # del user
# # print(user)

"""nested dict"""
# user_dict = {
#     1:
#         {
#              "name": "John",
#              "age": 32
#         },
#     2:
#         {
#             "name": "Peter",
#             "age": 21,
#             "addresses": ['Line 1', "line 2", 456006]
#         }
# }
# print(user_dict[1]['name'])
# print(user_dict[2]['addresses'][2])

"""loop """
user_dict = {'name': "Jhon", 'age': 28, "Country": "India", "phone_number": 123456789}
# for key in user_dict:
#     print(key, end=': ')
#     print(user_dict[key])

# for val in user_dict.values():
#     print(val)

# for val in user_dict.keys():
#     print(val)

# for key, val in user_dict.items():
#     print(key + ': ', val)

# merge two dict using unpacing
# d1 = {'name': 'jhone'}
# d2 = {'name': 'jhone', 'age': 28}
# d3 = {**d1, **d2}
# print(d3)

# # # map two list into dict
# keys = ['red', 'green', 'blue']
# values = ['#FF0000','#008000', '#0000FF']
# d = {}
# for x in keys:   # red
#     d[x] = values[keys.index(x)]   #d['red'] = values[0]
# print(d)


# using zip and variable length
# print(zip(keys, values))
# color_dictionary = dict(zip(keys, values))
# print(color_dictionary)


# dict comprehension
# squares = {x: x*x for x in range(6)}
# print(squares)



# dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
#
# double_dict1 = {k: v * 2 for (k, v) in dict1.items()}
# print(double_dict1)


# double_dict1 = {k*2: v for (k, v) in dict1.items()}
# print(double_dict1)


# dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# # Check for items greater than 2
# dict1_cond = {k:v for (k,v) in dict1.items() if v>2}
#
# print(dict1_cond)