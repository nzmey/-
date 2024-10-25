print('\n')

'''СЧЁТЧИК ВЫЗОВОВ.'''

calls = 0

def count_calls():
    global calls
    calls += 1
    return 0

def string_info(s):
    count_calls()

    f_s = ''
    f_s += s
    c = len(f_s)
    u = f_s.upper()
    l = f_s.lower()

    f_tupl = (c, u, l)
    return f_tupl

def is_contains(s, arg_list):
    count_calls()

    f_s = ''
    f_s += s
    f_l_s = s.lower()

    f_list = []
    f_l_list = []
    for i in range(len(arg_list)):
        f_list.append(arg_list[i])

    for j in range(len(f_list)):
        f_l_list.append(f_list[j].lower())

    f_bool = s in f_l_list
    return f_bool



'''RESULTS:'''

t = string_info('Hello Friends')
print(f'tupl = {t}')

b = is_contains('world', ['dog', 'WoRLD'])
print(f'bool = {b}')

t = string_info('Hello WORK')
print(f'tupl = {t}')

b = is_contains('Den', ['dog', 'World', 'Hello'])
print(f'bool = {b}')

t = string_info('Hello WoRLD')
print(f'tupl = {t}')

print(f'calls = {calls}')

