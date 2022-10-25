while True:
    print('''
    Вас приветсвует калькулятор!
    Выберите одну из доступных операций: + - * /
    ''')
    operation = input('Введите операцию: ')
    number1 = float(input('Введите первое число: '))
    number2 = float(input('Введите второе число: '))

    if operation == '+':
        print(number1 + number2)
    elif operation == '-':
        print(number1 - number2)
    elif operation == '*':
        print(number1 * number2)
    elif operation == '/':
        if number2 != 0:
            print(number1 / number2)
        else:
            print('Ошибка деления на ноль')
    else:
        print('Неизвестная операция')

print('Конец цикла')