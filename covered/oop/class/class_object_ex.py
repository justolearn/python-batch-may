# # check if emp has achieved weekly target or not (he need to make 5 weekly sale to achieve his target)
# class Employee:
#     """
#     Class Name: Employee with atrributes and method
#     """
#     """ attribute of employee """
#     name = "Ben"
#     designation = "Sales Executive"
#     salesMadeThisWeek = 6
#     """ action performed by employee"""
#     def has_achieved_target(self):
#         if self.salesMadeThisWeek > 5:
#             print("Target has been achieved")
#         else:
#             print("Target has not been achieved")
#
#
#
# # object instantiation
# employeeOne = Employee()
# # calling attributes and method of class
# print(employeeOne.name)
# print(employeeOne.designation)
# # invoke/call method
# employeeOne.has_achieved_target()
# # creating another object
# empTwo = Employee()
# print("employee two name: ", empTwo.name)


# # class attribute
# class Employee:
#     numberOfWorkingHours = 40
#
#
#
# emp_1 = Employee()
# emp_2 = Employee()
# print("emp one", emp_1.numberOfWorkingHours)
# print("emp two", emp_2.numberOfWorkingHours)
# # change class attribute
# Employee.numberOfWorkingHours = 45
# print("emp one", emp_1.numberOfWorkingHours)
# print("emp two", emp_2.numberOfWorkingHours)
# # # create instance attribute
# emp_1.name = "Ben"
# print("emp one name", emp_1.name)
# # # accessing emp_2 attribute before its creation
# # print("emp two name", emp_2.name)
# emp_2.name = "Jhon"
# print("emp two name", emp_2.name)
# # # Changing class attribute with object name
# emp_1.numberOfWorkingHours = 40
# print("emp one", emp_1.numberOfWorkingHours)
# print("emp two", emp_2.numberOfWorkingHours)



# # method without self parameter
# class Employee:
#     def employee_detail():
#         pass
#
#
# emp = Employee()
# emp.employee_detail()
# Employee.employee_detail(emp)


# # providing self
# class Employee:
#     def employee_detail(self):
#         self.name = "Jhon"
#         print("name is : ", self.name)
#
#
# emp = Employee()
# emp.employee_detail()
# Employee.employee_detail(emp)


# # create attribute without using self : age
# class Employee:
#     def employee_detail(self):
#         self.name = "Jhon"
#         print("name is : ", self.name)
#         age = 45
#         print("age is", age)
#
#     def print_emp_detail(self):
#         print(f'name is {self.name}')
#         print(f'age is {age}')
#
#
# emp = Employee()
# emp.employee_detail()
# emp.print_emp_detail()