first = 42
second = 69
third = 42
if first == second and first == third:
    y = input('Введите число три:  ')
    print('числа равны между собой')
elif first == second and first != third or first != second and first == third:
    y = input('Введите число два:  ')
    print(' два числа равны между собой')
elif first != second and first != third:
    y = input('Введите число ноль:  ')
    print('все числа неравны между собой')