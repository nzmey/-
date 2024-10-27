print('\n')

'''РАСПАКОВКА.'''

def print_params(a=1, b='строка', c=True):
    print(a, b, c)
    return 0

print('Вызовы функции print_params() с разным числом аргументов.')
print_params(34, 56, 28)
print_params(34, 56)
print_params(34)
print_params()
print('\n')

print('Распаковка параметров.')
values_list = [False, 78, 'Hello']
values_dict = {'a':56, 'b':[78, 34], 'c':'World'}
print_params(*values_list)
print_params(**values_dict)
print('\n')

print('Распаковка + отдельные параметры.')
values_list_2 = [23.12, 'Python']
print_params(*values_list_2, 42)


