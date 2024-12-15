print('\n')

'''   <<<  "Записать и запомнить"  >>>   '''

'''
I wandered lonely as a cloud
That floats on high o'er vales and hills,
When all at once I saw a crowd,
A host of golden daffodils;
Beside the lake, beneath the trees,
Fluttering and dancing in the breeze.

Continuous as the stars that shine
and twinkle on the Milky Way,
They stretched in never-ending line
along the margin of a bay:
Ten thousand saw I at a glance,
tossing their heads in sprightly dance.

'''


s_1 = 'I wandered lonely as a cloud'
s_2 = 'That floats on high over vales and hills,'
s_3 = 'When all at once I saw a crowd,'
s_4 = 'A host of golden daffodils;'
s_5 = 'Beside the lake, beneath the trees,'
s_6 = 'Fluttering and dancing in the breeze.'
s_7 = 'Continuous as the stars that shine'
s_8 = 'and twinkle on the Milky Way,'
s_9 = 'They stretched in never-ending line'
s_10 = 'along the margin of a bay:'
s_11 = 'Ten thousand saw I at a glance,'
s_12 = 'tossing their heads in sprightly dance.'

poem_list = [s_1, s_2, s_3, s_4, s_5, s_6, s_7, s_8, s_9, s_10, s_11, s_12]

name_file = "Poem_file.txt"
poem = open(name_file, 'w')
poem.write('')
poem.close()

# print(poem_list)

def custom_write(file_name, strings):
    from pprint import pprint
    cw_dict = {}
    # content = open(file_name, 'a')
    content = open(file_name, 'a', encoding = 'utf-8')
    n_str = 1
    for i in range(len(strings)):
        b = content.tell()
        content.write(strings[i])
        content.write('\n')
        cw_dict[(n_str, b)] = strings[i]
        n_str += 1

    content.close()

    print('\nЧтение ФАЙЛА:\n')
    content = open(file_name, 'r', encoding = 'utf-8')
    # content = open(file_name, 'r')
    pprint(content.read())
    content.close()

    return cw_dict

poem_dict = custom_write(name_file, poem_list)
print('\nСодержимое СЛОВАРЯ:\n')
for key, value in poem_dict.items():
    print(f'{key}\n{value}')
















