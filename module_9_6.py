print('\n')

'''   <<<  ГЕНЕРАТОРЫ.  >>>   '''

def all_variants(text):
    import itertools
    s = ''
    for i in range(len(text)):
        for v in itertools.combinations(text, i+1):
            for j in range(len(v)):
                s += v[j]
            yield s
            s = ''


s_1 = 'abc'
f_by_1 = all_variants(s_1)
print(s_1)
for v in f_by_1:
    print(v, ' ', end = '')

print('\n')

s_2 = 'world'
f_by_2 = all_variants(s_2)
print(s_2)
for v in f_by_2:
    print(v, ' ', end = '')

print('\n')

s_3 = 'begin'
f_by_3 = all_variants(s_3)
print(s_3)
for v in f_by_3:
    print(v, ' ', end = '')

print('\n')

s_4 = 'name'
f_by_4 = all_variants(s_4)
print(s_4)
for v in f_by_4:
    print(v, ' ', end = '')

print('\n')



