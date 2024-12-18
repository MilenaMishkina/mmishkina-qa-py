def addition(a, b):
    print(f'Результат суммы значений равен: {a + b}')

def subtraction(a, b):
    print(f'Результат разницы значений равен: {round(a - b, 2)}')

def division(a, b):
    if b ==0:
        print('На ноль делить нельзя!')
    else:
        print(f'Результат деления a на b равен: {round((a / b), 2)}')

def multiplication(a, b):
    print(f'Результат умножения значений равен: {a * b}')
