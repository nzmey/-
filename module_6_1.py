print('\n')

''' СЪЕДОБНОЕ - НЕСЪЕДОБНОЕ '''

'''... ой, ну их эти таксоны... растения, животные, хищники...
давайте лучше в "СЪЕДОБНОЕ - НЕСЪЕДОБНОЕ" поиграем...'''

class Food:

    eaten = True # Съеденный
    def food_bool(self):
        if self.eaten:
            return '... оставляет о себе одни только воспоминания...'
        else:
            return '... всё ещё ждёт своего поедателя...'

class Animal(Food):

    fed = False # Накормленный
    def fed_bool(self):
        if self.fed:
            return '... пребывает в Величайшем Блаженстве!!!'
        else:
            return '... не знает куда себя девать...'

    def is_eat(self, food):

        food.eaten = True

        if isinstance(self, Omnivorous):
            self.fed = True

        elif isinstance(self, Predator):
            if isinstance(food, NoFood):
                self.fed = False
            else:
                self.fed = True

        elif isinstance(self, Herbivores):
            if isinstance(food, IsFood):
                self.fed = True
            else:
                self.fed = False

        return  print(f' <<<  {self.name} и {food.name} >>>  \n'
                      f'{self.name} съедает {food.eat_name} и теперь {self.fed_bool()}.\n'
                      f'А {food.name} - {food.food_bool()}\n')

    def no_eat(self, food):

        self.fed = False
        food.eaten = False

        return  print(f' <<<  {self.name} и {food.name} >>>  \n'
                      f'{self.name} не поедает {food.eat_name},'
                      f' предпочитая голод и достойную жизнь.\n'
                      f'А {food.name} - {food.food_bool()}\n')


class Predator(Animal): # Хищники.

    def __init__(self, name = 'Хищник', eat_name = 'хищника'):
        self.name = name
        self.eat_name = eat_name
        self.__str__()

    def __str__(self):
        return print(f'{self.name}')


class Herbivores(Animal, Food): # Травоядные.

    def __init__(self, name = 'Травоядное', eat_name = 'травоядную'):
        self.name = name
        self.eat_name = eat_name
        self.__str__()

    def __str__(self):
        return print(f'{self.name}')


class Omnivorous(Animal, Food): # Всеядные.

    def __init__(self, name = 'Демон', eat_name = 'демона'):
        self.name = name
        self.eat_name = eat_name
        self.__str__()

    def __str__(self):
        return print(f'{self.name}')


class IsFood(Food): # Съедобные.

    def __init__(self, name = 'Фрукт', eat_name = 'фрукт'):
        self.name = name
        self.eat_name = eat_name
        self.__str__()

    def __str__(self):
        return print(f'{self.name}')


class NoFood(Food): # Несъедобные.

    def __init__(self, name = 'Камень', eat_name = 'камень'):
        self.name = name
        self.eat_name = eat_name
        self.__str__()

    def __str__(self):
        return print(f'{self.name}')



print('\n <<< НАШИ ПЕРСОНАЖИ  >>> ')

print('\nХИЩНИКИ:')
wolf = Predator('Волк', 'волка')
hawk =Predator('Ястреб', 'ястреба')

print('\nТРАВОЯДНЫЕ:')
cow = Herbivores('Корова', 'корову')
giraffe = Herbivores('Жираф', 'жирафа')
mouse = Herbivores('Мышь', 'мыша')

print('\nВСЕЯДНЫЕ:')
shark = Omnivorous('Акула', 'акулу')
barmaley = Omnivorous('Бармалей', 'Бармалея')
robin_bobin_barabek = Omnivorous('Робин Бобин Барабек', 'Робина Бобина Барабека')
demon = Omnivorous()

print('\nПРЕДМЕТЫ СЪЕДОБНЫЕ:')
banana = IsFood('Банан', 'банан')
clover = IsFood('Клевер', 'клевер')
oats = IsFood('Овёс', 'овёс')

print('\nПРЕДМЕТЫ НЕСЪЕДОБНЫЕ:')
stone = NoFood()
tower = NoFood('Башня', 'башню')

print('\n<<< РЕЗУЛЬТАТЫ ПОЕДАНИЯ  >>>\n')

wolf.is_eat(cow)
wolf.no_eat(cow)
wolf.is_eat(stone)
wolf.no_eat(stone)
hawk.is_eat(mouse)
hawk.no_eat(mouse)

shark.is_eat(barmaley)
shark.no_eat(barmaley)
robin_bobin_barabek.is_eat(tower)
robin_bobin_barabek.no_eat(tower)
demon.is_eat(barmaley)
demon.no_eat(barmaley)

giraffe.is_eat(banana)
giraffe.no_eat(banana)
cow.is_eat(clover)
cow.no_eat(clover)
mouse.is_eat(oats)
mouse.no_eat(oats)



'''<<< PS >>>'''
'''В текущем задании - по крайней мере - ДВЕ логические ошибки. 
Во-первых - среди млекопитающих есть как ХИЩНИКИ так и ТРАВОЯДНЫЕ.
А во-вторых - не все растения и фрукты годытся в пищу. Не говоря уже про цветы.
По сему поводу - предлагаю переделать данное задание - сообразно моему решению...
Или как-нибудь по другому.'''




