"""Print First 10 natural numbers using while loop"""
# i = 0
# while i < 10:
#     print(i)
#     i += 1

"""taken 10 inputs from user and print average"""
# sum1 = 0
# i = 10
# while i > 0:
#     print("Enter number")
#     num = int(input())
#     sum1 = sum1 + num
#     i = i - 1
# print("average is", sum1 / 10)

"""take input recurcively from user and exit when 0 is entered"""
# while True:
#     num = int(input('Enter a number : '))
#     if num == 0:
#         break
#     print("You enter : ", num)


"""Write a Python program that prints all the numbers from 0 to 6 except 3 and 6."""
# #
# # Note : Use 'continue' statement.
# for x in range(6):
#     if x == 3 or x == 6:
#         continue
#     print(x)

"""take list of numbers print whether list contains even or odd numbers"""
# l = [1, 3, 5]
# l = [2, 4, 6]
# for ele in l:
#     if ele % 2 == 0:
#         print("list contains an even number")
#         break
# else:
#     print("list does not contain an even number")

"""accept number from user and find sum of all the numbers from 1 to given numbers"""
# sum1 = 0
# n = int(input("Please enter number "))
# for i in range(1, n + 1):
#     sum1 += i
# print("Sum is: ", sum1)

"""print table of number taken input from user"""
# n = int(input("Enter number to calculate table : "))
# for i in range(1, 11):
#     product = n*i
#     print(product)