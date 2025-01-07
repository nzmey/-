print('\n')

'''   <<<  ДЕКОРАТОРЫ.  >>>   '''

def is_prime(func):

    def wrapper(a, b, c):
        res = func(a, b, c)
        print(f'Результат вычисления == "{res}"')
        # prime_list = (int(res%i == 0) for i in range(2, res//2+1))
        # print(f'prime_list = {list(prime_list)}')
        if (sum((int(res%i == 0) for i in range(2, res//2+1)))):
            print('Это СОСТАВНОЕ ЧИСЛО.\n')
        else:
            print('Это ПРОСТОЕ ЧИСЛО.\n')
        return res
    return wrapper


@is_prime
def sum_three(a, b, c):
    add = a + b + c
    return add

sum_three(4, 2, 7)
sum_three(4, 2, 6)

sum_three(19, 21, 13)
sum_three(31, 17, 9)

sum_three(15, 112, 24)
sum_three(62, 19, 78)

sum_three(222, 211, 34)
sum_three(119, 118, 234)

sum_three(352, 254, 127)
sum_three(168, 298, 271)




