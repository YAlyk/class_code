# # class Restaurant:
# #     def __init__(self):
# #         self.restaurant_name = 'Visota'
# #         self.cuisine_type = 'Italia'

# #     def describe_restaurant(self):
# #         print(self.restaurant_name)
# #         print(self.cuisine_type)

# #     def open_restaurant(self):
# #         print('ресторан открыт!')


# # r = Restaurant()
# # print(r.restaurant_name)
# # print(r.cuisine_type)
# # print()
# # r.describe_restaurant()
# # r.open_restaurant()
# # print('______________________')


# class Car():
#     # ...
#     def __init__(self, make, model, year):
#         # """Инициализирует атрибуты описания автомобиля."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.probeg = 0
#     def show_probeg(self):
#         # """Выводит пробег машины в милях."""
#         print("This car has " + str(self.probeg) + " miles on it.")
#     # def update_probeg(self, values):
#     #     self.probeg = values
#     def update_probeg(self, values):
#         self.probeg += values

# my_new_car = Car('audi', 'a4', 2016)
# my_new_car.show_probeg()

# my_new_car.probeg = 23
# my_new_car.show_probeg()

# my_new_car.update_probeg(20)
# my_new_car.show_probeg()
# my_new_car.update_probeg(3)
# my_new_car.show_probeg()

# str.upper()

class User():
    def __init__(self, first_name, last_name, Age):
        self.first = first_name
        self.last = last_name
        self.age = Age

    def describe_user(self):
        print(self.first_name, self.last_name, self.age)

    def greet_user(self):
        print("Hi " + self.first, self.last)


test = User('Jonh', 'Osborn', 30)
print(test.first)
test.greet_user()

test1 = User('Vasya', 'Pupkin', 10)
print(test1.greet_user())