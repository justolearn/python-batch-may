# # before initialization we are accessing
# class Employee:
#     def employee_detail(self):
#         self.name = "Jhon"
#
#     def print_emp_detail(self):
#         print(f'name is {self.name}')
#
#
# emp = Employee()
# emp.print_emp_detail()


# # intialize attributed before they are used
# class Employee():
#
#     def __init__(self):
#         self.name = "jhon"
#
#     def print_emp_detail(self):
#         print(f'name is {self.name}')
#
#
# emp = Employee()
# emp.print_emp_detail()
#
# # create another object
# emp_2 = Employee()
# emp_2.print_emp_detail()


# # Passing parameters to initialize
# class Employee:
#
#     def __init__(self, name):
#         self.name = name
#
#     def print_emp_detail(self):
#         print(f'name is {self.name}')
#
#
# emp = Employee('Mark')
# emp.print_emp_detail()
#
# # create another object
# emp_2 = Employee("Ben")
# emp_2.print_emp_detail()


# # object life cycle
class Employee(object):

    def __new__(cls, *args):
        print("new method", cls)
        return object.__new__(cls)

    def __init__(self, name):
        self.name = name
        print("init method", self)

    # def __str__(self):
    #     print('str method ', str(self.name))
    #     return str(self.name)

    def __del__(self):
        print("del method", self)

    def print_emp_detail(self):
        print(f'name is {self.name}')


emp = Employee('Mark')
# print(emp)
# emp_2 = Employee('ben')
# emp_2 = emp
# emp_3 = Employee('mark')


