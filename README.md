## Task_1:
Вычислить число Пи c заданной точностью d
Пример:
при d = 0.001, π = 3.141
при d = 0.1, π = 3.1
при d = 0.00001, π = 3.14154
d от 0.1 до 0.0000000001
!!ВНИМАНИЕ !!! не использовать константу math.pi
## Task_2:
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
## Task_3:
Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
исходной последовательности.
Пример:
47756688399943 -> [5]
1113384455229 -> [8,9]
1115566773322 -> []
## Task_4:
Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)
многочлена и записать в файл многочлен степени k
k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени
Записываем результат в файл.
Пример:
k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0
## Task_5:
Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов.
Пример двух заданных многочленов:
23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x + 33 = 0
Результат:
40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x + 53 = 0
