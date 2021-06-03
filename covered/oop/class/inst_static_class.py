# # instance method class method and static method
class MyClass:
    def ins_method(self):
        print("Instance method called ", self)

    @classmethod
    def cls_method(cls):
        print("Class method called ", cls)

    @staticmethod
    def static_method():
        print("Static method called ")


my_class_obj = MyClass()
"""calling instance method"""
# my_class_obj.ins_method()
# # MyClass.ins_method()   # will give error as instance is not provided
# MyClass.ins_method(my_class_obj)   # will run as instance is provided
# """ calling class method"""
# my_class_obj.cls_method()
# MyClass.cls_method()
# """ calling static method"""
# my_class_obj.static_method()
# MyClass.static_method()




""" instance method"""
# class Employee:
#
#     def employee_detail(self):
#         self.name = "Jhon"
#         print(self.name)
#
#
# ins_obj = Employee()
# ins_obj.employee_detail()


"""class method"""
# class Employee:
#     organization_name = "Google"
#
#     def employee_detail(self):
#         self.name = "Jhon"
#         print('inside instance method ',self.organization_name)
#         self.__class__.organization_name = "TCS"
#         print('inside instance method ',self.organization_name)
#
#
#     @classmethod
#     def change_organization_name(cls, name):
#         print("Previous organization name : ", cls.organization_name)
#         cls.organization_name = name
#         print("New organization name : ", cls.organization_name)
#
#
# ins_obj = Employee()
# ins_obj.employee_detail()
# # ins_obj.change_organization_name()
# ins_obj.change_organization_name('Microsoft')
# # # Can be called using class name
# # Employee.change_organization_name("Facebook")


"""static method"""
# class Employee:
#
#     def employee_detail(self):
#         self.name = "Jhon"
#         self.age = 30
#         print(f"Employee : {self.name} is {self.age} year old")
#
#     @staticmethod
#     def welcome_msg():
#         print("welcome to our organization!")
#
#
# ins_obj = Employee()
# ins_obj.employee_detail()
# ins_obj.welcome_msg()
# # calling by class name
# Employee.welcome_msg()