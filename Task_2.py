def check_for_input_error():
    while True:
        try:
            a = int(input('Введите любое натуральное число: '))
        except ValueError:
            print('Ошибка - необходимо ввести натуральное число!')
            continue
        if  a < 1:
            print('Ошибка - число должно быть положительным!')
            continue
        break
    return a
def simple_factors_list(a):
    my_list = []
    c = 2
    while c * c <= a:
        if a % c == 0:
            my_list.append(c)
            a //= c
        else:
            c += 1
    my_list.append(a)
    return my_list
N = check_for_input_error()
print(f'Список простых множителей для числа {N}: {simple_factors_list(N)}')