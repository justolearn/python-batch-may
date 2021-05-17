# While loop example
n = 5
sum = 0
i = 1
while i <= n:    # 1 <= 5 ; 2 <= 5; 3 <= 5; 4<=5; 5<=5; 6<=5
    sum = sum + i  #  sum = 1 ; 3; 3+3= 6
    i = i+1    #  i += 1
else:
    print("Condition evaluated as false")
print("The sum is", sum)


#
# n = 10
# while n > 0:
#     print(n)
#     n -= 1  # n = n-1

# while loop with else
# counter = 0
# while counter < 3:
#     print("Inside loop")
#     counter = counter + 1
# else:
#     print("Inside else")


# # break
# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i += 1
# # else block


# Continue
# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

