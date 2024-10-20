from typing import Union


def sum_of_two_nums(first_number: int|float, second_number: int|float):
    """Функция для вычисления суммы двух чисел"""
    print(first_number + second_number)


sum_of_two_nums(1.5, 3)


def max_num_in_list(list_of_numbers: list):
    """Функция для нахождения максимального числа в списке"""
    print(max(list_of_numbers))


num_list = [1, 20, 4]

max_num_in_list(num_list)


def say_hello(name:str):
    """Функция, которая принимает имя пользователя и выводит приветствие на экран"""
    print(f'Привет, {name}!')

test_name = 'Милена'

say_hello(test_name)