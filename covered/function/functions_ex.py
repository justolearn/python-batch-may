# def print_info():
#     print('Info')
#
#
# print_info()

# def print_info(name, age, company='TCS'):
#     print('name is : ', name)
#     print('Age is : ', age + 5)
#     print('Company is : ', company)
#
#
# # s= "Good morning"
# print_info("Jhon", age=28)
# print_info("Jhon", age=28, company = "Google")











# # function with parameters/arguments 4 types
# def print_info(msg):
#     print(f'[Info] {msg}')
#
#
# print_info("Hello world")

# # function with docstring and default arg
# def print_info(msg="default"):
#     """
#     :param msg:
#     :return: None
#     this function will print the passed message
#     """
#     print(f'[Info] {msg}')
#
#
# print_info()
# print(print_info.__doc__)


# function with return statement
# def add_num(num1, num2):
#     return num1 + num2
#
#
# # add_num(1, 2)
# result = add_num(1, 2)
# print(result)


# # function with multiple arguments
# def add_num(*args):
#     print(args)
#     total = 0
#
#     for n in args:
#         total = total + n
#
#     print("Sum:", total)
#
#
# add_num(3, 5)
# add_num(4, 5, 6, 7)
# add_num(1, 2, 3, 5, 6)
#
# a = (2, 3, 4, 5, 6)
# add_num(*a)

# # function with keyword argument
# def basic_detail(name='some name', msg="some message"):
#     print(f'name is {name} and message is {msg}')
#
#
# basic_detail('Good morning', 'jhon')
# basic_detail(msg='Good morning', name='jhon')


# # function with kwargs
# def basic_detail(**kwargs):
#     print("Data type of argument: ", type(kwargs))
#
#     for key, value in kwargs.items():
#         print("{} is {}".format(key, value))
#
#
# basic_detail(Firstname="Jhon", Lastname="Parker", Age=22, Phone=1234567890)
# basic_detail(Firstname="Sam", Lastname="Claw", Age=29, Phone=87656565667, Country="USA")
# a = {"Firstname":"Sam", "Lastname":"Claw", "Age":29, "Phone":87656565667, "Country":"USA"}
# basic_detail(**a)


# global and local variable
"""using global variable"""
# x = "global"
# def info():
#     print("x inside:", x)
#
#
# info()
# print("x outside:", x)

# changing inside func
# x = "global"
# def info():
#     x = 'local'
#     x = x*2
#     print("x inside:", x)
#
#
# info()
# print("x outside:", x)

# # local variable
# def info():
#     y = 'local'
#     print(y)
#
#
# info()
# print(y)


# global and local var
# x = "global"
#
#
# def info():
#     x = 'local'
#     print("x inside:", x)
#
#
# info()
# print("x outside:", x)


# Access global var inside func
# x = "global"
#
#
# def info():
#     global x
#     x = x*2
#     print(x)
#     x = 'local'
#     print("x inside:", x)
#
# print(x)
# info()
# print("x outside:", x)



# # call by value
# def func_1(num):
#     print(id(num))
#     print(num)
#     num = 30
#     print(num)
#     print('id x: ', id(num))
#
#
# x = 20
# print('x is outside', x)
# print(id(x))
# func_1(x)
# print('x is outside', x)
# print('x: ', id(x))


# # call by reference
# def func_2(num):
#     print(id(num))
#     num.append(30)
#     print(num)
#     num = []
#     print("new list ",num)
#     print(id(num))
#
#
# x = [20]
# print('x is ', x)
# print(id(x))
# func_2(x)
# print('x: ',x)
# # print('x id is  ', id(x))

