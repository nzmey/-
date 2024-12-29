print('\n')

'''   <<<  ВЫЗОВ РАЗОМ  >>>   '''

def  apply_all_func(int_list, *functions):
    result = {}
    func_list = []
    func_list.append(*functions)
    func_list = func_list[0]
    for i in func_list:
        result[i.__name__] = i(int_list)

    return result

func_list = [min, max, len, sum, sorted]

n_list = [21, 12, 6.345, 56, 7.28, 8, 74, 32, 9.45, 89]

res_dict = apply_all_func(n_list, func_list)

for key, value in res_dict.items():
    print(f'Key: {key}       Value: {value}')




