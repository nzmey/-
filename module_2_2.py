print('\n')

'''Задача ВСЕ РАВНЫ.'''

'''Вводим числа.'''
first = input('Введите первое число : ')
second = input('Введите второе число : ')
third = input('Введите третье число : ')

'''УСЛОВИЯ.'''
if first == second == third:
    print(3)
elif (first == second)or(second == third)or(first == third):
    print(2)
else:
    print(0)
