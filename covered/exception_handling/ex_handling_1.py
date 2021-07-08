
# 10 * (1/0)
# print(10+20)
# 4 + spam*3
# '2' + 2


# example
# try:
#     # 10 * (1/0)
#     # 4 + spam*3
#     '2' + 2
# except Exception as e:
#     print("exception : ", e)
#
# print(10+20)


# example
# try:
#     10 * (1 / 0)
#     print(x)
# except NameError:
#     print("Variable x is not defined")
# except Exception as e:
#     print("Something else went wrong ", e)


# example
# try:
#     a = 10
#     b = 0
#     # a/b
#     print(x)
# except NameError:
#     print("Variable x is not defined")
# except ZeroDivisionError:
#     print("Cannot be divided by zero")
# except:
#     print("Something else went wrong")



# try:
#     a = 10
#     b = 0
#     # a / b
#     # print(x)
# except NameError:
#     print("Variable x is not defined")
# except ZeroDivisionError:
#     print("Cannot be divided by zero")
# except:
#     print("Something else went wrong")
# else:
#     print("else block executed")
# finally:
#     print("Finally block executed")


# try:
#     '2' + 2
#     a = 10
#     b = 0
#     a/b
#     print(x)
# except (NameError, ZeroDivisionError) as e:
#     print("Variable x is not defined", e)
# except:
#     print("Something else went wrong")


# raise exception
# try:
#     raise NameError('Hi There')
# except NameError as e:
#     print('An exception flew by!', e)


# # example
# try:
#     a, b = 10, 0
#     if b == 0:
#         raise ZeroDivisionError('Cannot divide by zero')
#     raise NameError('Hi There')
# except NameError as e:
#     print('An exception flew by!', e)
# except ZeroDivisionError as e:
#     print("Exception ", e)


# # raise Exception
# def functionName(level):
#     if level < 1:
#         raise Exception("Invalid level! " + str(level))
#
#
# try:
#    functionName(0)
# except Exception as e:
#    print("Exception :", e)


