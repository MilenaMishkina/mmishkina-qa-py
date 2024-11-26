num = int(input())
if num > 0:
    print('Число положительно')
else:
    print('Число отрицательное')

num = int(input())
if num < 0:
    print('Число отрицательное')
elif num == 0:
    print('Число равно нулю')
elif num > 0 and num < 10:
    print('Число от 1 до 9')
else:
    print('Число 10 и больше')