print('\n')

'''   <<<   "Найдёт везде"  >>>   '''

'''
It's a text for task Найти везде,
Используйте его для самопроверки.
Успехов в решении задачи!
text text text

'''

class WordsFinder:

    def __init__(self, *files):
        self.file_names = []
        self.file_names.append(list(files))
        self.file_names = self.file_names[0]
        self.show_name()
        self.get_all_words(switch = 1)

    def show_name(self):
        print('\n\n  <<<   ЭТО ИМЕНА ДОСТУПНЫХ ФАЙЛОВ   >>>\n')
        for i in range(len(self.file_names)):
            print(self.file_names[i])
        print('\n\n   <<<   А ВОТ ИХ СОДЕРЖИМОЕ    >>>')
        for i in range(len(self.file_names)):
            print('\n\n\n',self.file_names[i],'\n')
            with open(self.file_names[i], encoding = 'utf-8') as fl:
                print(fl.read())


    def get_all_words(self, switch = 1):
        dict_all_words = {}
        all_list = []
        s = ''
        s_1 = ''
        s_2 = ''
        for i in range(len(self.file_names)):
            with open(self.file_names[i], encoding = 'utf-8') as fl:
                d_key = fl.name
                s = (fl.read())
                s_1 += s.lower()
                for j in range(len(s_1)):
                    if s_1[j] == ',' or s_1[j] == '.' or s_1[j] == '=' or s_1[j] == '!' \
                    or s_1[j] == '?' or s_1[j] == ';' or s_1[j] == ':' or s_1[j] == '—' :
                        continue
                    elif j == ' ':
                        s_2 += s_1[j]
                    else:
                        s_2 += s_1[j]

                all_list = s_2.split()

                dict_all_words[d_key] = all_list
                all_list = []
                s = ''
                s_1 = ''
                s_2 = ''

        if switch :
            for key, value in dict_all_words.items():
                print(f'\n   <<<   ФАЙЛ "{key}" СОДЕРЖИТ СЛЕДУЮЩИЕ СЛОВА   >>>\n\n{value}\n')

        return dict_all_words

    def find(self,  f_word):
        number = 0
        cnt = 1
        dict_find = {}
        dict_list = self.get_all_words(switch = 0)
        for i in range(len(self.file_names)):
            content = dict_list[self.file_names[i]]
            '''
            Если есть желание проверить точность подсчёта - 
            можно раскомментировать ниже написанный код.
            '''
            # n = 1
            # print('\n\n',self.file_names[i], '\n')
            # for k in range(len(content)):
            #     print(f'{n} {content[k]} | ', end='\n')
            #     n +=1
            for j in range(len(content)):
                if content[j] == f_word.lower():
                    number = cnt
                    break
                else:
                    cnt += 1
                    continue

            dict_find[self.file_names[i]] = number
            number = 0
            cnt = 1
        print('\n')
        for key, value in dict_find.items():
            if dict_find[key] == 0:
                print(f'В файле {key} слово {f_word} - не встречается.')
            else:
                print(f'В файле "{key}" - слово "{f_word}" встречается первый раз на {value} месте.')

        return dict_find

    def count(self,  c_word):
        cnt = 0
        number = 0
        place = ''
        dict_count = {}
        dict_list = self.get_all_words(switch = 0)
        for i in range(len(self.file_names)):
            content = dict_list[self.file_names[i]]
            '''
            Если есть желание проверить точность подсчёта - 
            можно раскомментировать ниже написанный код.
            '''
            n = 1
            # print('\n\n',self.file_names[i], '\n') # Раскомментировать !!!
            for j in range(len(content)):
                # print(f'{n} {content[j]} | ', end='\n') # Раскомментировать !!!
                if content[j] == c_word.lower():
                    cnt += 1
                    place += str(n)
                    place += ', '
                    # print(f'{n} {content[j]}_____{cnt} | ', end='\n') # Раскомментировать !!!
                n += 1

            number = cnt
            dict_count[self.file_names[i]] = [number, place]
            cnt = 0
            number = 0
            place = ''
            n = 1
        print('\n')

        for key, value in dict_count.items():
            if dict_count[key][0] == 0:
                print(f'В файле {key} слово {c_word} - не встречается.')
            elif  1 < dict_count[key][0]%10 < 5:
                print(f'В файле "{key}" - слово "{c_word}" повторяется {value[0]} раза.')
                print(f'Находясь на {(value[1])}- месте.')
            else:
                print(f'В файле "{key}" - слово "{c_word}" повторяется {value[0]} раз.')
                print(f'Находясь на {(value[1])}- месте.')

        return dict_count

    def show_files(self, n_file, n_word):
        show_dict = {}

        return show_dict



finder_test = WordsFinder("test_file.txt")
finder_test.find('text')
finder_test.count('text')

finder = WordsFinder("Mother Goose - Monday’s Child.txt",
                     "Rudyard Kipling - If.txt",
                     "Walt Whitman - O Captain! My Captain!.txt")

finder.find('the')
finder.count('the')
finder.find('if')
finder.count('if')
finder.find('captain')
finder.count('captain')
finder.find('Child')
finder.count('Child')

'''PS'''
'''
В стихотворении про капитана на 105 месте затисался ДЕФИС, вместо ТИРЕ.
А в стихотворении Киплинга - слово "the" первый раз встречаетс на "107" а не на "109" месте.
Причина - в ДВУХ пропущенных ТИРЕ.

'''




