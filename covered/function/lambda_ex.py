# def raise_to_power(x, y):
#     return x ** y
#
#
# print(raise_to_power(2, 3))


# """convert into lambda function"""
# raise_to_power = lambda x, y: x ** y
# print(raise_to_power(2, 3))


# # square
# square = lambda n: n * n
# # print(square)
# num = square(5)
# print(num)


# # list of list
# a = [[4, 52], [24, 13], [2,1]]
# a.sort()
# print(a)


# def sort_first(a):
#     return a[1]
#
# a = [[4, 52], [24, 13], [2,1]]
# a.sort(key=sort_first)
# print(a)
#
# """lambda"""
# a = [[4, 52], [24, 13], [2,1]]
# a.sort(key=lambda x: x[1])
# print(a)
