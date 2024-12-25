print('\n')

'''   <<<  ПЛАН ПЕРЕХВАТ >>>   '''

def personal_sum(numbers):
    common = []
    result = 1
    incorrect_data = 0
    if isinstance(numbers, dict):
        f_keys = numbers.keys()
        f_values = numbers.values()
        common += f_keys
        common += f_values
    else:
        common += numbers
    for r in range(len(common)):
        try:
            result += common[r]
        except TypeError:
            print(f'Некорректный тип данных: {type(common[r])}.')
            incorrect_data += 1
            continue

    result -= 1

    return (result, incorrect_data)


def calculate_average(numbers):
    f_list = []
    temp_cnt = 0
    cnt = 0
    if isinstance(numbers, dict):
        f_keys = numbers.keys()
        f_values = numbers.values()
        f_list += f_keys
        f_list += f_values
        temp_cnt = len(f_keys) + len(f_values)
    else:
        try:
            f_list += numbers
            temp_cnt = len(numbers)
        except TypeError:
            print(f'Изначально некорректный тип данных: {type(numbers)} !!!')
            return None
        finally:
            f_list = []

    f_tuple = personal_sum(numbers)
    result = 0
    cnt = temp_cnt - f_tuple[1]
    # print(f'CNT = {cnt}')
    try:
        result = f_tuple[0] / cnt
    except ZeroDivisionError:
        print(f'Деление на нуль. Число некорректных данных = <{f_tuple[1]}>')
        return 0
    else:
        print(f'Число некорректных данных = <{f_tuple[1]}>')
        return result
    finally:
        f_list = []


result_1 = calculate_average([24, 34, "Hello"])
print(f'Result_1 = <{result_1}>\n')

test_dict = {'Den':1, "Mary":2, 'Nick':30, 14:7}

result_2 = calculate_average(test_dict)
print(f'Result_2 = <{result_2}>\n')

result_3 = calculate_average("23, 12, 18")
print(f'Result_3 = <{result_3}>\n')

result_4 = calculate_average([])
print(f'Result_4 = <{result_4}>\n')

result_5 = calculate_average((34, "Hello", test_dict, 12))
print(f'Result_5 = <{result_5}>\n')

result_6 = calculate_average(254)
print(f'Result_6 = <{result_6}>\n')


