# regex - регулярные выражения

# . - означает любой символ
# \d - находит любое число
# \D - любой нечисловой символ
# ^ - начало шаблона
# $ - конец шаблона
# {4} - колв-во символов в шаблоне (любое числовое значение)
# \W - любой символ но не буквы и не числа
# \w - все буквы и числа
# [] - указывают последовательность сиволов

import re

# match проверяет начинается ли строка с определённого шаблона в
# в примере с love он возвращает None

# text = "I lo ve Bishkek! lo ve nazgul@gmail.com lo ve asdas"

# x = re.match("love", text)
# print(x.group(0))

# search - ищет шаблое в какой либо строке, находит только первый по порядку подстроку

# x = re.search(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", text)
# print(x.group(0))

# .findall - возвращает список с найденными паттернами

# x = re.findall(r"(lo)", text)
# print(x)

# Задача найти спящий бичи найти при помощи regex

# with open("pushkin.txt", "r") as file:
#     text = file.read()
#     sleeping = re.findall(r"спящий", text)
#     print(sleeping)
#     axe = re.findall(r"бич", text)
#     print(axe)

# .split() разделяет строку, по указанному сепаратору
# x = re.split("lo", text)
# print(x)

# x = re.split("lo", text, maxsplit=2)
# print(x)

# .sub() - заменяет шаблон на что-то
# x = re.sub("lo | ve", "gg", text)
# print(x)


# \+996\(55+[1-9]\)-\d{3}-\d{3} -regex

with open("some_text.txt", "r") as file:
    text = file.read()
    found_numbers = re.findall(r"\+996\(55+[1-9]\)-\d{3}-\d{3}", text)

with open("some_new_text", "a") as file:
    file.write(str(list(map(lambda x: x.replace("-", " "), found_numbers))) + "\n")


