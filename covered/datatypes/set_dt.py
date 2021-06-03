# s = {}
# print(type(s))
# s1 = set()
# print(type(s1))

# set1 = {"apple", "banana", "cherry"}
# set2 = {1, 5, 7, 9, 3}
# set3 = {True, False, False}
# set4 = {1, 'Apple', False, 'False', 1, 'apple'}
# # #
# print(set1)
# print(set2)
# print(set3)
# print(set4)
# print(type(set4))
#
#
# t = ('t1', 1, 'Apple', 'Apple')
# print(t)
# s = set(t)
# print(s)

"""converting string into set"""
# s = "Hello world"
# print(s)
# print(set(s))


"""accessing set"""
# set4 = {1, 'Apple', False, 'False', 1, 'apple'}
# for s in set4:
#     print(s)


# set is mutable but object inside set is immutable no list
# s = {1, 2, "hello"}
# print(s)

"""set method"""
"""add method"""
# s1 = {"hello", 1, "apple"}
# print(s1)
# s1.add('Banana')
# print(s1)



"""update method"""
# s1 = {"hello", 1, "apple"}
# s2 = {"banana", "apple", 2, 1}
# s3 = [1,2,3]
# # s4 = ("hello", 1, 3)
# s5 = "hello"
# s1.update(s5)
# print(s1)

"""Removing elements from a set"""
# s1 = {"banana", "apple", 2, 1}
# s1.discard(1)
# print(s1)
# s1.discard(1)
# print(s1)   # discarding the element not present in set will not give any error
# s1 = {"banana", "apple", 2, 1}
# s1.remove(2)
# print(s1)
# s1.remove(2)
# print(s1)   # removing the element not present in set will give  error


"""set operators
Union"""
# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}
# print(a | b)
#
"""or """
# print(a.union(b))
# print(b.union(a))


"""Intersection"""
# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}
#
# print(a & b)
# print(a.intersection(b))

"""difference"""
# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}
# print(a - b)
# print(b - a)
# print(a.difference(b))
# print(b.difference(a))

"""symmetric difference of two sets"""
# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}
# print(a ^ b)
# print(a.symmetric_difference(b))

"""membership in set"""
# s1 = set("apple")
# print(s1)
# print('a' in s1)
#
# s2 = {'1', 'apple', 2}
# print('apple' in s2)
# print('1' in s2)
# print(3 in s2)

"""sum method"""
# s1 = {2, 1}
# print(len(s1))
# print(sum(s1))

"""frozenset"""
# a = frozenset([1, 2, 3, 4])
# b = frozenset([3, 4, 5, 6])
# print(a)
# print(a | b)
# print(a.add(9))

