print('\n')

'''...ИЗМЕНИТЬ - НЕЛЬЗЯ - ПОЛУЧАТЬ...'''

class Vehicle:

    owner = 'User'
    __model = 'locomotive'
    __color = 'WHITE'
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
                 __model = 'ЗИЛ'    , #Vehicle._Vehicle__model
                 __color = Vehicle._Vehicle__color,
                 __engine_power = Vehicle._Vehicle__engine_power ): # Это самые безобидные инициации.
                                                                    # На get-функции компилятор ругается.
        Vehicle.owner = owner
        Vehicle.__model =  'BMW'   #__model
        Vehicle.__color = __color
        Vehicle.__engine_power = __engine_power
        Vehicle.print_info()


print('\nКатим наши паровозы...')
sedan_1 = Sedan()
sedan_2 = Sedan('Max', 'BMW', 'BLACK', 500) # Как мне его инициализировать?
                                            # Кроме атрибута "owner" - поменять ничего нельзя.

print('\nМеняем владельца нашего паровоза...')
sedan_1.owner = 'Den'

print('Меняем цвет нашего паровоза:')
sedan_1.set_color('Red')
sedan_1.set_color('Green')

print('\nЧто же нам остаётся...')
sedan_1.print_info()


''' <<<  PS >>> '''
'''Я бы назвал эту тему просто: "ИНКАПСУЛЯЦИЯ".'''
''' ... Интересно, а можно всё-таки изменить значения приватных атрибутов - желательно в конструкторе -
    - без лишней головной боли?... типа - прописывать специальные методы в дочернем классе ...
    ... и так далее ...
'''