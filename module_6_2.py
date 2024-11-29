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
        return print(f'{self.get_model()},   '
                     f'{self.get_horsepower()},   '
                     f'{self.get_color()},   '
                     f'Владелец: {self.owner}')

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

    def __init__(Vehicle,
                 owner = Vehicle.owner,
                 __model = Vehicle._Vehicle__model,
                 __color = Vehicle._Vehicle__color,
                 __engine_power = Vehicle._Vehicle__engine_power ):
        Vehicle.owner = owner
        Vehicle._Vehicle__model = __model
        Vehicle._Vehicle__color = __color
        Vehicle._Vehicle__engine_power = __engine_power
        Vehicle.print_info()

    # def __init__(Vehicle):
    #     Vehicle.print_info()

print('\nКатим наши паровозы...')

vehicle = Vehicle()

sedan_1 = Sedan()
# print(Sedan.mro())
# print(Sedan.__mro__)
sedan_2 = Sedan('Max', 'BMW', 'BLACK', 500)

print('\nМеняем владельца нашего паровоза...')
sedan_1.owner = 'Den'

print('Меняем цвет нашего паровоза...')
sedan_1.set_color('Red')
sedan_1.set_color('Green')

print('\nЧто же нам остаётся...')
sedan_1.print_info()

print('\nА старый паровоз - остался старым паровозом...')
vehicle.print_info()
print('\nТаким же - как и старый СЕДАН...')
sedan_3 = Sedan()


''' <<<  PS >>> '''
'''Я бы назвал эту тему просто: "ИНКАПСУЛЯЦИЯ".'''



