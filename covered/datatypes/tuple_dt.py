# empty tuple
# tup1 = ()
# print(tup1)
#
# # tuple with 1 element
# tup1 = (50,)
# print(tup1)
# print(type(tup1))
#
# t1 = (5, 'program', 1 + 3j)

# # accessing values
# print(t1[0])

# # slicing
# print(t1[::-1])
# print(t1[1:2])
# t = (0, 1, 2, 3, 5, 7)
# # doesnt perform assignment
# # t[0:3] = (5, 'program', (1+3j))
# print("t[0:3] = ", t[0:3])


# # updating tuple
# tup1 = (12, 34.56)
# tup2 = ('abc', 'xyz')

# Following action is not valid for tuples as they are immutable
# tup1[0] = 100

# # concatenate
# tup3 = tup1 + tup2
# print(tup3)

# # del
# tup = ('Python', 'Java', 1, 2)
# print(tup)
# del tup
# # print("After deleting tup : ")
# print(tup)

# # len
# tup = ('Python', 'Java', 1, 2)
# print(len(tup))

# # repetition
# t1 = (1,)
# print(t1 * 4)

# # membership
# tup = ('Python', 'Java', 1, 2)
# print(1 in tup)

# # iteration
# tup = ('Python', 'Java', 1, 2)
# for x in tup:
#     print(x)

# # different ways to print
# tup = ('Python', 'Java', 1, 2)
# print(tup)
# print(*tup)

# # Min/max
# t1 = (1, 2, 3)
# print(min(t1))
# print(max(t1))

# # convert a list in tupple
# a = [1, 2, 3, 6, 5, 4]
# print(a)
# print(tuple(a))

# can change value of mutable object inside immutable object
# t = (5,'program', [1,'hello'])
# # print(id(t[2]))
# print(t)
# t[2][1] = 'a'
# print(t)
# t[2] = 6
# t[2].append('b')

# count occurrence of element
# t = (50, 10, 60, 70, 50)
# print(t.count(50))

# index of element
# t = (50, 10, 60, 70, 50)
# print(t.index(10))


# t, a, *b = (1, 2, 3, 4, 5)
# print(t)
# print(a)
# print(b)

