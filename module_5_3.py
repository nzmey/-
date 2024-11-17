print('\n')

'''НУЖНО БОЛЬШЕ ЭТАЖЕЙ!!!'''
'''Дом у бабушки моей просит много этажей!!!...'''


class House:
    def __init__(self, name = 'House', number_of_floors = 10, capital = 10, ceo = 'Den', tr = 0):
        self.name = name
        self.number_of_floors = number_of_floors
        self.capital = capital
        self.ceo = 'Den'
        self.tr = tr
        if self.tr == 0:
            print(self.__str__())

    def __str__(self):
        return f'МЫ - "{self.name}" !!!...\n' \
            f'Наша этажность равна {self.number_of_floors}... \n' \
            f'Наш капитал равен {self.capital} миллионам зелёными !!!... \n' \
            f'МЫ КРУЧЕ ВСЕХ !!!...\n'

    def __bool__(self, bl = True):
        if bl == True:
            return 'ДА'
        elif bl == False:
            return 'НЕТ'

    def __eq__(self, other):  # (==)
        return self.__bool__(self.number_of_floors == other.number_of_floors)
    def __lt__(self, other):  # (<)
        return self.__bool__(self.number_of_floors < other.number_of_floors)
    def __le__(self, other):  #(<=)
        return self.__bool__(self.capital <= other.capital)
    def __gt__(self, other):  #(>)
        return self.__bool__(self.number_of_floors > other.number_of_floors)
    def __ge__(self, other):  #(>=)
        return self.__bool__(self.capital >= other.capital)
    def __ne__(self, other):  #(!=)
        return self.__bool__(self.number_of_floors != other.number_of_floors)


    def __add__(self, other):        # Сложение (+).
        if isinstance(other, House): # - увеличивает кол-во этажей.
            self.number_of_floors += other.number_of_floors
        elif isinstance(other, int): # - увеличивает капитал.
            self.capital += other
        return self

    def __radd__(self, value): #
        return self
    def __iadd__(self, other): #
        return self


    def __sub__(self, other):        # Вычитание (-).
        if isinstance(other, House): # - Уменьшает число этаэей.
            self.number_of_floors -= other.number_of_floors
        elif isinstance(other, int): # - Уменьшает капитал.
            self.capital -= other
        return self

    def __rsub__(self, value): #
        return self0
    def __isub__(self, value): #
        return self


    def __mul__(self, other):        # Умножение (*).
        if isinstance(other, House): # - Умножает число этаэей.
            self.number_of_floors *= other.number_of_floors
        elif isinstance(other, int): # - Умножает капитал.
            self.capital *= other
        return self

    def __rmul__(self, value): #
        return self
    def __imul__(self, value): #
        return self


    def __floordiv__(self, other):   # Целочисленное деление (//).
        if isinstance(other, House): # - Делит число этажей.
            self.number_of_floors //= other.number_of_floors
        elif isinstance(other, int): # - Делит капитал.
            self.capital //= other
        return self

    def __rfloordiv__(self, value): # Целочисленное деление.
        return self
    def __ifloordiv__(self, value): # Целочисленное деление.
        return self


    def sos_floors(self):
        return print('Караул!!! Нас ужимают!!!')

    def sos_capitals(self):
        return print('Караул!!! Нам обрезают капитал!!!')



House(capital = 375)
house_1 = House()
house_2 = House()
house_by_country = House('Домик в деревне', 3, 800)
house_by_river = House('Дом на набережной', 23, 200)
house_on_hill = House('Дом на холме', 54, 500)
add_ = House('++', 8)
sub_ = House('--', 18)
mul_ = House('*', 7)
div_ = House('/', 3)

print('Только посредственности всегда равны!!! Правильно?...')
print(house_1 == house_2)

print('\nСреди настоящих людей и строений - никогда не бывает равных!!! Верно?...')
print(house_on_hill != house_by_country)

print('\nДомик в деревне иногда бывает больше самых высоких домов на холмах...')
print( house_by_country > house_on_hill)

print('\nОднако, если ему добавить немножко этажей...')
house_by_country + add_

print('\nДа ещё эти этажи на что-нибудь помножить...')
house_by_country * mul_

print('\nТо его капитал - может солидно увеличиться!...')
house_by_country + 150
print(f'И составить {house_by_country.capital} миллионов зелёными!...')

print('\nА ежели одного его конкурента слегка поджать....')
house_on_hill - sub_
print(house_on_hill)
house_on_hill.sos_floors()

print('\nА другого конкурента солидно поделить.....')
house_by_river // 2
print(house_by_river)
house_by_river.sos_capitals()

print('\nТо, на фоне остальных - он может выглядеть даже очень весьма солидно....')
print(house_by_country)

print('\nНапример, - капиталом - превзойти всех... Точно?...')
print(house_by_country >= house_on_hill)
print(house_by_river <= house_by_country)

print('\nДа и этажностью солидно выделяться... Ведь правда же?...')
print(house_by_country > house_on_hill)
print(house_by_river < house_by_country )

print(f'\nПусть даже капитал компании "{house_by_river.name}"\n'
      f'теперь больше капитала компании "{house_on_hill.name}"...\n'
      f'Возможно ли такое?...')
print(house_on_hill <= house_by_river)

print(f'\nДа и этажностью компания "{house_by_river.name}"\n'
      f'сильно превосходит компанию "{house_on_hill.name}"...\n'
      f'Правда?...')
print(house_on_hill < house_by_river)

print(f'\nА "{house_by_country.name}" - всё равно больше всех!... И это великая истина!...')
print(house_by_country >= house_by_river)
print(house_by_country >= house_by_river)
print(house_by_country > house_by_river)
print(house_by_country > house_by_river)


print(f'\nНу, а Генеральный Директор всего этого безобразия {House(tr = 1).ceo} -\n'
      f'благодарит вас и нас за посещение всего этого безобразия...')


print('\nВСЁ!!! БОЛЬШЕ НЕ МОГУ... КРЫША ЕДЕТ!!!....')

