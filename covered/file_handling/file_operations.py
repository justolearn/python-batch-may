# # open file in read mode
# file = open('test.txt', 'r')
# for each in file:
#     print(each)

# # other way to read a file
# file = open("test.txt", "r")
# print(file.read())
# file.write("hello") # error as file is on read mode
# print(file.readline())


# # read() mode character wise
# file = open("test.txt", "r")
# print(file.read(6))


# # creating a file using write mode
# file = open('write_ex.txt', 'w')
# file.write("This is the write command. \n")
# file.write("It allows us to write in a particular file")
# file.close()

# # creating a file return error if file exist
# file = open('write_ex.txt', 'x')
# file.write("This is the write command. \n")
# file.write("It allows us to write in a particular file")
# file.close()


# # append() mode
# file = open('test.txt','a')
# file.write("This will add this line")
# file.close()


# # tell and seek method
# file = open('test.txt', 'r')
# print(file.read())
# print(file.tell()) # current position
# print('read next ', file.read())
# print(file.seek(0))
# print(file.read())


# # reading file using with()
# with open("test.txt") as file:
#     data = file.read()
#     print(data)
# # do something with data

# # write file using with function
# with open("test.txt", "w") as f:
#     f.write("Hello World!!!")

# # append file using with
# with open("test.txt", "a") as f:
#     f.write(" Hello World!!!")

# # read and write mode
# with open("test.txt", "r+") as f:
#     print(f.read())
#     f.write("Hello World!!!")
#     f.close()


