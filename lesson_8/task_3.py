# Задание 3:
# Создайте original.txt и запишите в него любую информацию.
# Напишите программу, которая копирует все содержимое файла original.txt в copy.txt.

with open("original.txt", "r") as original, open("copy.txt", "w+") as copy:
    copy.write(original.read())
    print(copy.read())
