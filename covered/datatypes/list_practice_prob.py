# # 1. sum of list using python sum function
# print(sum([1, 2, 3, 4, 5]))


# # 2. print second highest number in list
# a = [3, 2, 6, 1, 8, 4, 9, 5]
# a.sort()
# print(a[-2])


# # 8. enter number and print respective day from list
# num = int(input("Enter a number between 1-7 : "))
# day_list = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
# if 0 < num <= 7:
#     print(day_list[num-1])
# else:
#     print("enter a valid number")


# # 3. even/odd number
# list1 = [10, 21, 4, 45, 66, 93, 11]
# print([num for num in list1 if num % 2 == 0])
# # 4. print number of even/odd number
# list1 = [10, 21, 4, 45, 66, 93, 11]
# only_odd = [num for num in list1 if num % 2 != 0]
# odd_count = len(only_odd)
# print("Even numbers in the list: ", len(list1) - odd_count)
# print("Odd numbers in the list: ", odd_count)

#
# # print flatten list of planets whole length is less than 6
# planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']]
# # using for loop
# new_planet_list = []
# for planet_list in planets:
#     for planet in planet_list:
#         if(len(planet)<6):
#             new_planet_list.append(planet)
#
# print(new_planet_list)
# # using list comprehension
# print([planet for planet_list in planets for planet in planet_list if len(planet)<6])


# 5. print all negative number in list
# list1 = [-10, -21, -4, 45, -66, 93]
# neg_nos = [num for num in list1 if num < 0]
# print(neg_nos)


# # 6. program to return duplicates from list
# a = [10, 20, 10, 30, 40, 50, 30, 50, 40, 60, 70]
# new_list = []
# for num in a:
#     if a.count(num) > 1 and num not in new_list:
#         new_list.append(num)
# print(new_list)

# # 7. program to remove duplicates from list
# output
# a = [10, 20, 10, 30, 40, 50, 30, 50, 40, 60, 80,  70]
#
#
#
# new_list = []
# for num in a:
#     if num not in new_list:
#         new_list.append(num)
# print(new_list)


# # 9. swap first and list element of list
# day_list = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
# day_list[0], day_list[-1] = day_list[-1], day_list[0]
# print(day_list)


# 10. swap two element from list
# first_pos = int(input("enter First pos : ")) - 1
# second_pos = int(input("enter Second pos : ")) - 1
# day_list = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
#
# day_list[first_pos], day_list[second_pos] = day_list[second_pos], day_list[first_pos]
# print(day_list)
