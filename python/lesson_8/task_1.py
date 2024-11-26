# Задание 1:
# Создайте текстовый файл с именем data.txt и наполните его несколькими строками текста.
# Напишите программу, которая открывает файл, читает его построчно и принтит каждую строку.

with open('data.txt', 'r') as file:
    result = file.read()
    print(result)

# или

result = open('data.txt', 'r')
print(result.read())
