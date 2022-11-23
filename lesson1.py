# frozenset

# set
# set_a = {1, 2, 3, 4, "Nazgul"}
# set_b = frozenset([3, 4, "Nazgul"])
#
# print(set_a.isdisjoint(set_b))

# zip встроенная функция

# list_1 = ["apple", "banana", "Nazgul"]
# list_2 = ["tomato", "potato"]
#
# print(dict(zip(list_1, list_2)))

# recursion

# input_num: int = int(input("Введите желаемое число: "))
# # for i in range(1, input_num + 1):
# #     print(i)
# counter = 1
#
#
# def generate_num (input_number: int):
#     if input_number == 0:
#         return input_number
#     else:
#         print(input_number)
#         return generate_num(input_number - 1)
#
#
# print(generate_num(input_num))

# Задача 1

# number: int = int(input("Введите желаемое число: "))
#
#
# def get_factorial(number: int):
#     if number == 1:
#         return number
#     else:
#         output_number = number * get_factorial(number - 1)
#         return output_number
#
#
# print(get_factorial(number))

# Задача 2

# list_of_numbers = [1, 2, 3, 5]
#
# def get_sum(list_of_numbers: list):
#     if len(list_of_numbers) == 0:
#         return 0
#     else:
#         summed_value = list_of_numbers[0] + get_sum(list_of_numbers[::])
#         return summed_value
#
#
# print(get_sum(list_of_numbers))

# Решение от ментора:

# list_a = [1, 2, 3, 6]
#
#
# def get_sum(lists: list):
#     if lists == []:
#         return 0
#     else:
#         get_result = get_sum(lists[1:])
#         sum = get_result + lists[0]
#         return sum
#
#
# print(get_sum(list_a))

# Задача на числа Фибоначчи:

# 1, 1, 2, 3, 5, 8

# def get_row_of_fibonacci(some_int: int):
#     res_list = []
#     if some_int == 1:
#         res_list += [1, 1]
#         return res_list
#     else:

# json

# import json
#
# with open("test.json", "r") as file:
#     new_dict = json.load(file)
#
# new_dict["name"] = "Zamira"
# new_dict["age"] = 17
# new_dict["is_18"] = True
#
# with open("test.json", "w") as file:
#     text_json = json.dumps(new_dict, indent=4)
#     file.write(text_json)
















