tuple_ex = (1, 2, 3, 4, 5)

# output (5, 4, 3, 2, 1)
# print(tuple_ex[::-1])

tuple_ex = ("Orange", [1, 2, 3], (25, 15, 5))
# output 2
# print(tuple_ex[1][1])

# Create a tuple with single item 50
t = (50,)
# print(type(t))

#  Unpack the following tuple into 4 variables
t_ex = (10, 20, 30, 40)
# 10
# 20
# 30
# 40


# swap two tuples
t1 = (100, 200)
t2 = (20, 30)

# t1 = (20, 30)
# t2 = (100, 200)
t1, t2 = t2, t1


# Copy element 4 and 5 from the following tuple into a new tuple
tuple1 = (1, 2, 3, 4, 5, 6)
t2 = tuple1[3:6]

# modify 22 to 222
t_1 = (1, [22, 32], 4, 5)
t_1[1][0] = 222


# a = 5   # a = 5 + 0j
# print(type(a))
# print(a.real)
# print(a.imag)
# print(id(a))

# print(type(range(3)))
