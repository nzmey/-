print('\n')

'''   <<<  Функциональное разнообразие.  >>>   '''

print('Лямбда - фнукция:')

first  = 'Мама мыла раму'
second = 'Рамена мало было'
res_list =  list(map( lambda x, y: list(x) == list(y), first, second))
print(f"res_list = {res_list}")



print('\nЗамыкание:')

def get_advanced_writer(file_name):
    s = str(file_name)
    def write_everything(*data_set):
        with open(s, 'w') as fl:
            fl.write(str(data_set))

    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

with open('example.txt', 'r') as n_fl:
    print(f'Зачитываем файл "{n_fl.name}":  {n_fl.read()}')




print('\nМетод "__call__" позволяющий использовать КЛАСС как Функцию:')

class MysticBall:

    def __init__(self, *words):
        self.words = words
        self.__call__()

    def __call__(self):
        import random
        i = random.randint(0, len(self.words) - 1)
        s = str(self.words[i])

        return s

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())




