print('\n')

'''ИСТОРИЯ СТРОИТЕЛЬСТВА.'''

class House:

    __houses_history = []

    def __new__(cls,name = 'House', number_of_floors = 10, capital = 10, ceo = 'Den', tr = 0):
        cls. name = name
        if tr == 0:
            cls.__houses_history.append(cls.name)
        return super().__new__(cls)

    def __init__(self, name = 'House', number_of_floors = 10, capital = 10, ceo = 'Den', tr = 0):
        self.name = name
        self.number_of_floors = number_of_floors
        self.capital = capital
        self.ceo = 'Den'
        self.tr = tr

        if self.tr == 0:
            print(self.__str__())


    def __del__(self):
        if self.tr == 0:
            return print(f'Строительный трест {self.name} - уничтожен...\n'
                         f'НО ПАМЯТЬ О НЁМ ОСТАНЕТСЯ В ВЕКАХ!!!...\n')


    def __str__(self):
        return f'МЫ - "{self.name}" !!!...\n' \
            f'Наша этажность равна {self.number_of_floors}... \n' \
            f'Наш капитал равен {self.capital} миллионам зелёными !!!... \n' \
            f'МЫ КРУЧЕ ВСЕХ !!!...\n'


    def fc_memory(self):
        print('ВЕЧНАЯ ПАМЯТЬ ВСЕМ УНИЧНОЖЕННЫМ!!!...')
        for i in self.__houses_history:
                print(f'"{i}".')



house_1 = House()
house_2 = House(capital = 375)
house_by_country = House('Домик в деревне', 3, 800)
house_by_river = House('Дом на набережной', 23, 200)
house_on_hill = House('Дом на холме', 54, 500)


del house_1
del house_2
del house_by_country
del house_by_river
del house_on_hill

print(f'Список "ВНЕСЁННЫХ..." в книгу "ПАМЯТИ...": {House._House__houses_history}.....\n')

House(tr=1).fc_memory()




