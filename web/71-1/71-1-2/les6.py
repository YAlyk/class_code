# class Car:
#     pass

# a = Car().__dir__
# print(a)

# class Juice:
#     def __init__(self, ingredient=None):
#         if ingredient is not None:
#             self.ingredient = ingredient
#         else:
#             self.ingredient = None

#     def my_juice(self):
#         if self.ingredient != None:
#             print("Сок с {}".format(self.ingredient))
#         else:
#             print("Сок без добавки")


# drink_1 = Juice("малиной")
# drink_2 = Juice()
# drink_1.my_juice()
# drink_2.my_juice()


class Student:
    name = "Ivan"
    age = 18
    group_number = "10A"

    def get_Name(self):
        print(Student.name)

    def get_Age(self):
        print(Student.age)

    def get_Group_number(self):
        print(Student.group_number)

    def set_Name_Age(self, a, b):
        Student.name = a
        Student.age = b

    def set_Group_number(self, a):
        Student.group_number = a


student_1 = Student()
student_1.get_Name()
student_1.get_Age()
student_1.get_Group_number()
student_1.set_Name_Age("Masha", 19)
student_1.set_Group_number("FN1")
student_1.get_Name()
student_1.get_Age()
student_1.get_Group_number()
