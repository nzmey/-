print('\n')


'''  <<<  ГЕНЕРАТОР ПСЕВДО-СЛУЧАЙНЫХ ЧИСЕЛ. >>>  '''

num = bin(1048576)
print(num)
num = bin(1048575)
print(num)

print('\nФункция генератор Заданного количества псевдо-случайных чисел:\n')
def random_nz_test(number_of_number = 10):
    from time import sleep
    from time import time

    state = int(time())% 1048575
    number = 0
    cnt = 0
    n_d = 0
    s = ''
    cnt_dict = {}
    repeat_dict = {}
    collector = []
    repeat = []
    repeat_1 = []
    '''Количество случайных чисел.'''
    while cnt < number_of_number:
        for _ in range(20):
            bit_1 = state & 1
            s += str(bit_1)
            # print(bit_1, end = '')
            new_bit = (state^(state>>1)^(state>>2)^(state>>7)) & 1
            state = (state>>1)|(new_bit<<19)

        print('')
        number = int(s, 2)
        number = int(number)

        if number in repeat:
            repeat_1.append(number)

        if number in collector:
            repeat.append(number)
            repeat_dict[cnt] = number


        collector.append(number)
        print(f'"{cnt}"')
        print(s)
        print(number)
        s = ''
        cnt += 1
        if number > 999999:
            cnt_dict[cnt] = number
        sleep(1)

    print('\nNumber > 999999:')
    for key, value in cnt_dict.items():
        print(f'N {n_d}: cnt = {key-1}, number = {value}')
        n_d += 1

    n_d = 0
    print('\nRepeat number:')
    print(repeat_1)

    for key, value in repeat_dict.items():
        print(f'Number {n_d}: Cnt = {key-1} value = {value}. ')
        n_d += 1

    n_d = 0

    return number

'''Генерит ЗАДАННОЕ КОЛИЧЕСТВО случайных чисел.'''
print('Генерация ЗАДАННОГО количества случайных чисел:')
result = random_nz_test(20)


print('\nГенератор одного СЛУЧАЙНОГО числа.')
def random_nz(t = 1):
    from time import sleep
    from time import time

    state = int(time()) % 1048575
    number = 0
    cnt = 0
    s = ''
    while cnt < t:
        for _ in range(20):
            bit_1 = state & 1
            s += str(bit_1)
            new_bit = (state ^ (state >> 1) ^ (state >> 2) ^ (state >> 7)) & 1
            state = (state >> 1) | (new_bit << 19)

        number = int(s, 2)
        number = int(number)
        s = ''
        cnt += 1

    return number

'''Генерит ОДНО случайное число.'''
print('\nГенерация ОДНОГО случайного числа:')
result_2 = random_nz()
print(f'Result 2 = {result_2}.')




