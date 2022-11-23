# class
# моносостояние

# class Car:
#     _property_cars = {
#         "model": "VAZ",
#         "color": "blue"
#     }
#
#     def __init__(self):
#         self.__dict__ = Car._property_cars
#
#
# car1 = Car()
# car2 = Car()
#
# print(car2.__dict__)
# print(car1.__dict__)
# print(car1.model)
# car1.model = "sdaksm"
# print(car1.model)
# print(car1.__dict__)
# print(car2.__dict__)

# dunder methods eq hash

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __eq__(self, other):
#         if isinstance(other, Point):
#             return self.x == other.x and self.y == other.y
#
#     def __hash__(self):
#         return hash((self.x, self.y))
#
#
# point1 = Point(12, 6)
# point2 = Point(12, 6)
#
# print(hash(point1))
# print(point1.__hash__())


# Mixin-ы
users = {}


class RegisterMixin:
    def validate_username(self):
        if self.username in users.keys():
            print("Такой пользователь уже существует")
            return False
        return True


class Register(RegisterMixin):

    def __init__(self, name, age, username):
        self.name = name
        self.age = age
        self.username = username

    def save_to_dict(self):
        users.update(
            {
                self.username: {
                    "name": self.name,
                    "age": self.age
                }
            }
        )

    def save_in_validated_data(self):
        if self.validate_username():
            self.save_to_dict()
            return f"{self.username} was saved"
        return f"{self.username} was not saved"


nazgul = Register("Nazgul", 26, "aveid")
print(nazgul.save_in_validated_data())
chyngyz = Register("Chyngyz", 20, "chika")
print(chyngyz.save_in_validated_data())
syimyk = Register("Syimyk", 18, "senior html developer")
print(syimyk.save_in_validated_data())

print(users)

# 1. Write a class called Investment with fields called principal and interest.
# The constructor should set the values of those fields.
# There should be a method called value_after that
# returns the value of the investment after n years.
# The formula for this is p(1 + i)
# n
# , where p is
# the principal, and i is the interest rate.
# It should also use the special method str so that
# printing the object will result in something like below:
# Principal - $1000.00, Interest rate - 5.12%

# 2. Write a class called Product. The class should have fields called name, amount, and price,
# holding the product’s name, the number of items of that product in stock, and the regular
# price of the product.
#
# There should be a method get_price that receives the number of
# items to be bought and returns a the cost of buying that many items, where the regular price
# is charged for orders of less than 10 items, a 10% discount is applied for orders of between
# 10 and 99 items, and a 20% discount is applied for orders of 100 or more items. There should
# also be a method called make_purchase that receives the number of items to be bought and
# decreases amount by that much.

# Задача 1


class Investment:
    def __init__(self, interest, principal):
        self.interest = interest
        self.principal = principal

    def value_after(self, n):
        return self.principal * (1 + self.principal) * n

    def __str__(self):
        return f"Principal - {self.principal}$\nInterest rate - {self.interest}%"


investment_1 = Investment(6, 1000)
print(investment_1)
print(investment_1.value_after(7))


# Задача 2


class Product:
    def __init__(self, name, amount, price,
                 holdings_product_name, amount_in_stock, regular_price):
        self.name = name
        self.amount = amount
        self.price = price
        self.holdings_product_name = holdings_product_name
        self.amount_in_stock = amount_in_stock
        self.regular_price = regular_price

    def get_price(self, amount):
        if amount >= 10:
            return amount * self.regular_price
        elif 10 < amount < 100:
            return amount * self.regular_price - round(amount * self.regular_price * 0.1)
        elif 100 < amount:
            return amount * self.regular_price - round(amount * self.regular_price * 0.2)

    def make_purchase(self, amount_to_be_bought):
        return f"The rest of product in stock - {self.amount_in_stock - amount_to_be_bought}"


laptop = Product(
    "Lenovo",
    100,
    400,
    "Laptop's shop",
    50,
    500
)

print(laptop.get_price(15))
print(laptop.make_purchase(15))




