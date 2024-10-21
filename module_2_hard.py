print('\n')

'''СЛИШКОМ СТАРЫЙ ШИФР...'''

def f_pass_word(n, m):

    print('\nHello, friends!!!\n\n')

    '''Этот объект - функция должна вернуть в виде СПИСКА...'''
    '''...в который входят СПИСОК и СЛОВАРЬ...'''
    RESULT = []


    '''Готовим СЛОВАРЬ и его аргументы...'''
    res_dict = {}
    key_list = []
    value_list = []

    '''Готовим СПИСОК и его содержимое...'''
    res_list = []
    '''Содержимое СПИСКА...'''
    source_list = []
    factor_res_list = []
    add_res_list = []
    int_res_list = []

    '''Временные списки...'''
    m_list = []
    add_list = []
    int_list = []

    '''Формируем список ИСХОДНЫХ "СЛУЧАЙНЫХ" ЧИСЕЛ...'''
    for i_s in range(n, m):
        source_list.append(i_s)
    # Копируем список ИСХОДНЫХ "СЛУЧАЙНЫХ" ЧИСЕЛ в список ключей СЛОВАРЯ...
    key_list = source_list

    '''Формируем список МНОЖИТЕЛЕЙ...'''
    for i_m in range(n, m):
        m_list = []
        for j_m in range(3, m+1):
            if i_m % j_m == 0:
                m_list.append(j_m)
            else:
                continue
        # Добавляем список МНОЖИТЕЛЕЙ для конкретного числа в ОБЩИЙ СПИСОК МНОЖИТЕЛЕЙ...
        factor_res_list.append(m_list)

    '''Вычисляем ПАРОЛИ...'''
    add = 0
    sub = 0
    pass_word_int = 0
    for i in range(len(factor_res_list)):

        sub = 0

        for s in range(int(i/2)+1):

            sub += 1

            for j in range(len(factor_res_list[i])):

                add = factor_res_list[i][j]
                if (add/2 - sub) > 0:
                    add_list.append(sub)
                    add_list.append(add - sub)
                else:
                    continue

#        print(f'{source_list[i]} - {factor_res_list[i]} - {add_list}')
#        print(f'{source_list[i]} - {add_list}')
#        print(f'{source_list[i]} - {int(str(add_list))}')

        # Добавляем ВЫЧИСЛЕННЫЙ ПАРОЛЬ в виде списка в ОБЩИЙ СПИСОК, содержащий СПИСКИ ПАРОЛЕЙ...
        add_res_list.append(add_list)

        # Преобразуем СПИСОК в ЕДИНОЕ ЧИСЛО и добавляем это число в СПИСОК ПАРОЛЕЙ...
        pass_word_int = int(''.join(map(str, add_list)))
        int_res_list.append(pass_word_int)
        value_list = int_res_list

        # Обнуление временного списка и временного пароля...
        add_list = []
        c_int = 0

    '''Пакуем РЕЗУЛЬТИРУЮЩИЙ СПИСОК...'''
    res_list.append(source_list)
    res_list.append(factor_res_list)
    res_list.append(add_res_list)
    res_list.append(int_res_list)

    '''Пакуем СЛОВАРЬ...'''
    for d in range(len(key_list)):
        res_dict[key_list[d]] = value_list[d]

    '''Распаковываем СЛОВАРЬ для проверки...'''
    for key,value in res_dict.items():
        print(f'Key = {key}, Value = {value}')


    '''Пакуем RESULT...'''
    RESULT.append(res_list)
    RESULT.append(res_dict)

    print('\n\n')

    return RESULT


'''Вызываем функцию ПАРОЛЕЙ...'''
res = f_pass_word(3, 21)

print('Только МНОЖИТЕЛИ...\n')
for i in range(len(res[1])):
    print(f'{res[0][0][i]} - {res[0][1][i]}')

print('\n\nМНОЖИТЕЛИ и СПИСКИ...\n')
for i in range(len(res[1])):
    print(f'{res[0][0][i]} - {res[0][1][i]} - {res[0][2][i]}')

print('\n\nТолько СПИСКИ...\n')
for i in range(len(res[1])):
    print(f'{res[0][0][i]} - {res[0][2][i]}')

print('\n\nТолько ГОТОВЫЕ ПАРОЛИ...\n')
for i in range(len(res[1])):
    print(f'{res[0][0][i]} - {res[0][3][i]}')

print('\n\n\n')

def f_game(d):
    r = None
    rr = None
    while True:
        r = input('Будете играть в игру?\n'
                  'Если будете - введите "y"... Если нет - введите "n"\n\n.')
        if r == 'y' or r == 'Y':
            while True:
                k = int(input('Введите число от 3 до 21...\n'))
                print(f'Паролем для числа {k} является число {d[k]}.\n\n')

                while True:

                    rr = input('Хотите ещё сыграть?\n\n')

                    if rr == 'y' or rr == 'Y':
                        break
                    elif rr == 'n' or rr == 'N':
                        print('Ну, как хотите...')
                        return 0
                    else:
                        print('НЕ ПОНЯЛ... ???... !!!')
                        continue

        elif r == 'n' or r == 'N':
            print('Ну, как знаете...')
            return 0
        else:
            print('НЕ ПОНЯЛ... ???... !!!')
            continue


'''Вызываем ИГРОВУЮ функцию...'''
f_game(res[1])


'''Ну, пожалуй, на этом можно и закончить... а то крыша совсем съедет...'''

