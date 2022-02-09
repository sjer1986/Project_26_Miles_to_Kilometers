# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
# #
# # print(add(500, 500, 500, 500, 500, 500, 500))
#
# def calculate(n, **kwargs):
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     # print(n)
#
# calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", color="Blue", seats="5", model="Skyline")
print(my_car.make)
print(my_car.model)
print(my_car.color)
print(my_car.seats)
