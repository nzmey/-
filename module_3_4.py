print('\n')

'''ОДНОКОРЕННЫЕ.'''

def single_root_words(root_word , *other_words):
    same_words = []
    test_word = ''
    root = ''
    root += root_word
    root = root_word.lower()

    for i in range(len(other_words)):
        test_word += other_words[i]
        test_word = test_word.lower()
        if root in test_word:
            same_words.append(other_words[i])
            test_word = ''
        elif test_word in root:
            same_words.append(other_words[i])
            test_word = ''
        else:
            test_word = ''
            continue

    return same_words


word_list_1 = ['Машина', 'поМОст', 'КРЫШа', 'еХАТЬ', 'Мостик', 'холоДильник', 'мостоваЯ', 'ШвейНая']
root_1 = 'МОСт'
word_list_2 = ['Шкаф', 'КОФЕ', 'мАШИНА', 'доМ', 'кРан']
root_2 = 'Кофемашина'

result_1 = single_root_words(root_1, *word_list_1)
print(f'Result_1: {result_1}.')
print(f'Word_list_1: {word_list_1}.')
print(f'Root_1: {root_1}.')
print('\n')

result_2 = single_root_words(root_2, *word_list_2)
print(f'Result_2: {result_2}.')
print(f'Word_list_2: {word_list_2}.')
print(f'Root_2: {root_2}.')



