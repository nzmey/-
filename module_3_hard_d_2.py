print('\n')

'''ЗАГЛАВИЕ: "Раз, два, три, четыре, пять .... Это не всё?".'''

data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}),
"Hello", ((), [{(2, 'Urban', ('Urban2', 35))}]) ]

def calculate_structure_sum(arg = None):

    first = 0
    f_str = '0'
    str_int = '0'
    counter = 0
    tr = 0

    if arg == None:
        return None

    else:

        f_str += str(arg)
        print(f'F_str ===== {f_str}')

        for i in f_str:

            if i == "'":
                tr += 1

                if tr > 2:
                    first += counter
                    tr = 0
                    counter = 0
                    continue

            elif tr > 0:
                tr += 1
                counter +=1

            elif 47 < ord(i) < 58:
                str_int += i

            else:
                first += int(str_int)
                str_int = '0'
                continue

        return first




result_t = calculate_structure_sum()
print(result_t)

result = calculate_structure_sum(data_structure)
print(result)
