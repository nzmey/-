print('\n')

'''...ИЗМЕНИТЬ - НЕЛЬЗЯ - ПОЛУЧАТЬ...'''

class Vehicle:

    owner = 'User'
    __model = 'locomotive'
    __color = 'WHITE_L'
    __engine_power = int(100)
    __COLOR_VARIANTS = ['BLUE', 'GREEN', 'WHITE', 'BLACK']

    def get_model(self):
        return str(f'Модель: {self.__model}')

    def get_horsepower(self):
        return str(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        return str(f'Цвет: {self.__color}')

    def print_info(self):
        print(f'{self.get_model()},   '
              f'{self.get_horsepower()},   '
              f'{self.get_color()},   '
              f'Владелец: {self.owner}')
        return 0

    def  set_color(self, new_color):

        if new_color.upper() in self.__COLOR_VARIANTS:
            old_color = self.__color
            self.__color = new_color.upper()
            print(f'Цвет "{old_color}" успешно заменён на цвет "{self.__color}" .')
        else:
            print(f'Невозможно поменять цвет "{self.__color}" на цвет "{new_color.upper()}" !!!')
        return self.__color

class Sedan(Vehicle):

    __PASSENGERS_LIMIT = 5

    def __init__(self,
                 owner = Vehicle.owner,
                 __model = Vehicle._Vehicle__model,
                 __color = Vehicle._Vehicle__color,
                 __engine_power = Vehicle._Vehicle__engine_power ):
        self.owner = owner
        self._Vehicle__model = __model
        self._Vehicle__color = __color
        self._Vehicle__engine_power = __engine_power
        self.print_info()
        self.get_passengers_limit()

    def get_passengers_limit(self):
        print(f'Ограничение пассажиров: {self.__PASSENGERS_LIMIT}')
        return 0

    def __str__(self):
        if isinstance(self, Sedan):
            self.print_info(), self.get_passengers_limit()
        else:
            self.print_info()
        return ''

    '''Этот конструкто не будет работать, так как в Базовом классе - конструктор отсутствует.'''
    # def __init__(self, owner = None, __model = None, __color = None, __engine_power = None):
    #     super().__init__( owner, __model, __color, __engine_power)

    '''Этот конструктор не инициализирует закрытые атрибуты класс "Vehicle" в экземпляре класса "Sedan".'''
    # def __init__(Vehicle):
    #     Vehicle.print_info()




print('\nКатаем наши паровозы...')

print('\nЭто старый паровоз:')
vehicle_1 = Vehicle()
vehicle_1.print_info()

print('\nА это вроде бы новый СЕДАН:')
sedan_1 = Sedan()
# print(Sedan.mro())
# print(Sedan.__mro__)

print('\nА это - уж совсем новый СЕДАН:')
sedan_2 = Sedan('Max', 'BMW', 'BLACK', 500)

print('\nМеняем владельца наших СЕДАНОВ...')
sedan_1.owner = 'Den'
sedan_2.owner = 'Den'

print('Меняем цвет наших СЕДАНОВ...')
sedan_1.set_color('Red')
sedan_1.set_color('Green')
sedan_2.set_color('Red')
sedan_2.set_color('Green')

print('\nЧто же нам остаётся...')
# sedan_1.print_info()
# sedan_2.print_info()
print(sedan_1.__str__())
print(sedan_2.__str__())

print('\nА старый паровоз - остался старым паровозом...')
vehicle_2 = Vehicle()
vehicle_2.print_info()

print('\nТаким же - как и старый СЕДАН...')
sedan_3 = Sedan()


''' <<<  PS >>> '''
'''Я бы назвал эту тему просто: "ИНКАПСУЛЯЦИЯ".'''



