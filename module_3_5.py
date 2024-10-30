print('\n')

'''РЕКУРСИВНОЕ УМНОЖЕНИЕ ЦИФР.'''

def get_multiplied_digits(number = None):
    str_number = ''
    str_number += str(number)
    first = 0
    if number == None:
        return None
    elif len(str_number) == 1:
        first = int(str_number[0])
        return first
    else:
        first = int(str_number[0])

        while int(str_number[len(str_number)-1]) == 0:
            str_number = str_number[:(len(str_number)-1)]

        if int(str_number[0]) == 0:
            get_multiplied_digits(int(str_number[1:]))
        else:
            return first * get_multiplied_digits(int(str_number[1:]))


result = get_multiplied_digits(2045032000)
print(f'result = {result}')


