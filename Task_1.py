def check_for_input_error():
    while True:
        try:
            a = float(input('Введите число по образцу "0.001", выставив нужное количество нулей в дробной части: '))
        except ValueError:
            print('Ошибка - необходимо ввести число!')
            continue
        if  a >= 1 or a <= 0:
            print('Ошибка - введите число по образцу!')
            continue
        break
    return a
import math
Pi = str(math.pi)
d = str(check_for_input_error())
print(math.pi)
print(Pi)
print(type(Pi))
print(d)
print(type(d))
print(f'Вывод числа π по введенному образцу: {float(Pi[:len(d)])}')