def check_for_input_error():
    while True:
        try:
            a = int(input('Задайте последовательность цифр: '))
        except ValueError:
            print('Ошибка - необходимо ввести только цифры!')
            continue
        return a
def get_unique_collection(my_list):
    unique_list = []
    viewed_list = []
    for i in my_list:
        if i not in viewed_list:
            viewed_list.append(i)
            unique_list.append(i)
        else:
            if i in unique_list:
                k = unique_list.index(i)
                del unique_list[k]
    return unique_list
roll = [int(x) for x in str(check_for_input_error())]
print(f'Список неповторяющихся элементов заданной последовательности: {get_unique_collection(roll)}')