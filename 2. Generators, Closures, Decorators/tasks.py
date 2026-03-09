# print("--- Завдання 1 --- Частина 1 ---")
# Створіть функцію, яка повертає всі парні числа в діапазоні. Функція приймає початок і кінець діапазону як параметри. Використовуйте механізм генераторів усередині функції.

# def even_numbers(start, end):
#     numbers = list(range(start, end))
#     for i in numbers:
#         if i % 2 == 0:
#             yield i

# for i in even_numbers(1,10):
#     print(i, end=" ")


# print("--- Завдання 2 --- Частина 1 ---")
# Створіть функцію, яка повертає всі значення зі списку, що знаходяться в діапазоні, зазначеному користувачем. Функція приймає список, початок і кінець діапазону як параметри. Використовуйте механізм генераторів усередині функції.

# def number_in_range(mylist, start, end):
#     number_range = list(range(start, end))
#     for item in mylist:
#         if item in number_range:
#             yield item

# numbers = {2,3,4,5,6}
# for i in number_in_range(numbers, 1, 10):
#     print(i, end=" ")


# print("--- Завдання 3 --- Частина 1 ---")
# Для виконання цього завдання обов'язково використовуйте механізм функцій вищого порядку (higher order functions). Створіть функцію, яка перевіряє на парність або непарність передане число. Користувач визначає на що перевіряти (парність або непарність).

# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False

# def is_odd(number):
#     if number % 2 != 0:
#         return True
#     else:
#        return False

# def check_value(value_to_check, function_to_call):
#     return function_to_call(value_to_check)

# value = int(input("Введіть число: "))
# choice = input("Перевірити на (even/odd): ")

# if choice == "even":
#     result = check_value(value, is_even)
# else:
#     result = check_value(value, is_odd)

# print(result)


# print("--- Завдання 4 --- Частина 1 ---")
# Створіть функцію для відображення поточного часу. Функція не приймає параметрів. Не використовуючи синтаксис декораторів, виконайте декорування функції за допомогою іншої функції. Потенційне виведення даних на екран:

# import datetime

# def decorator(func):
#     def wrapper():
#         print("="*30)
#         func()
#         print("="*30)
#     return wrapper

# def show_time():
#     print(datetime.datetime.now())

# show_time = decorator(show_time)

# show_time()


# print("--- Завдання 5 --- Частина 1 ---")
# До завдання 4 додайте ще одну функцію для декорування виведення даних. Ця функція має додати нові елементи у форматування виведення.

# import datetime

# def decorator(func):
#     def wrapper():
#         print("="*30)
#         func()
#         print("="*30)
#     return wrapper

# def decorator_2(func):
#     def wrapper():
#         print("~"*30)
#         func()
#         print("~"*30)
#     return wrapper

# def show_time():
#     print(datetime.datetime.now())

# show_time = decorator_2(decorator(show_time))

# show_time()


# print("--- Завдання 6 --- Частина 1 ---")
# Виконайте завдання 4, але з використанням синтаксису декораторів.

# import datetime

# def decorator(func):
#     def wrapper():
#         print("="*30)
#         func()
#         print("="*30)
#     return wrapper

# @decorator
# def show_time():
#     print(datetime.datetime.now())

# show_time()


# print("--- Завдання 1 --- Частина 2 ---")
# Створіть функцію, яка повертає всі прості числа в діапазоні. Функція приймає початок і кінець діапазону як параметри. Використовуйте механізм генераторів усередині функції.

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# def prime_numbers(start, end):
#     for number in range(start, end + 1):
#         if is_prime(number):
#             yield number

# for num in prime_numbers(1, 10):
#     print(num)


# print("--- Завдання 2 --- Частина 2 ---")
# Створіть функцію, яка повертає всі числа Армстронга в діапазоні. Функція приймає початок і кінець діапазону як параметри. Використовуйте механізм генераторів усередині функції.

# def is_armstrong(num):
#     digits = str(num)
#     power = len(digits)
    
#     total = 0
#     for digit in digits:
#         total += int(digit) ** power
#     if total == num:
#         return True
#     return False

# def armstrong_numbers(start, end):
#     for number in range(start, end + 1):
#         if is_armstrong(number):
#             yield number

# for num in armstrong_numbers(120,160):
#     print(num, end=' ')


# print("--- Завдання 3 --- Частина 2 ---")
# Для виконання цього завдання обов'язково використовуйте механізм функцій вищого порядку (higher order functions). Створіть функцію, яка знаходить мінімум або максимум у списку. Користувач визначає на що перевіряти (мінімум або максимум).

# def is_min(number_list):
#     min = number_list[0]
#     for i in range(len(number_list)):
#         if number_list[i] < min:
#             min = number_list[i]
#     return min

# def is_max(number_list):
#     max = number_list[0]
#     for i in range(len(number_list)):
#         if number_list[i] > max:
#             max = number_list[i]
#     return max

# def check_value(value_to_check, function_to_call):
#     return function_to_call(value_to_check)

# my_list = [2,23,2,4,51,5,12,51,52,5,12,3,23,32,1,95,5,8]
# choice = input("Перевірити на (max/min): ")

# if choice == "max":
#     result = check_value(my_list, is_max)
# else:
#     result = check_value(my_list, is_min)

# print(result)


# print("--- Завдання 4 --- Частина 2 ---")
# Створіть додаток із випікання піци. Кожна піца містить різні компоненти. Вико­ристовуючи механізм декораторів створіть різні піци:

# def decorator(func):
#     def private_decorator():
#         print("Піцца - ", end="")
#         func()
#     return private_decorator

# @decorator
# def margarita():
#     print("Маргарита")

# @decorator
# def four_chesse():
#     print("Чотири сира")

# margarita()
# four_chesse()
    