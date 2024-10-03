# Задание 2:
# Напишите скрипт, который запрашивает у пользователя его имя и возраст, а затем записывает эту информацию в файл userinfo.txt.
# Каждая запись должна быть отдельной строкой в файле.

while True:
    name = input()
    if name == '':
        break
    age = input()
    if age == '':
        break
    else:
        file = open("userinfo.txt", "a+")
        file.write(f"{name}:{int(age)}\n")
        print(file.read())
        file.close()




