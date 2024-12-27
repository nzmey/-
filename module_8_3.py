print('\n')

'''   <<<  НЕКОРРЕКТНОСТЬ.  >>>   '''

class IncorrectVinNumber(Exception):

    pass

class IncorrectCarNumbers(Exception):

    pass


class Car:

    def __init__(self,  model, vin_number, numbers):
        self.model = model
        self.__vin = self.__is_valid_vin(vin_number)
        self.__number = self.__is_valid_numbers(numbers)

    def __str__(self):
        return f'Model: {self.model}, VIN: {self.__vin}, Number: {self.__number}.'

    def  __is_valid_vin(self, vin_number):
        if isinstance(vin_number, int):
            if 999999 < vin_number < 10000000:
                return vin_number
            else:
                raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            raise IncorrectVinNumber('Некорректный тип vin номер')

    def  __is_valid_numbers(self, numbers):
        if isinstance(numbers, str):
            if len(numbers) == 6:
                return numbers
            else:
                raise IncorrectCarNumbers('Неверная длина номера')
        else:
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')


try:
    car_1 = Car("BMW", 777.777, "FM1278")
except IncorrectVinNumber as v:
    print(f'ПЕРЕХВАТ ИСКЛЮЧЕНИЯ IncorrectVinNumber:  {v}')
except IncorrectCarNumbers as n:
    print(f'ПЕРЕХВАТ ИСКЛЮЧЕНИЯ IncorrectCarNumbers:  {n}')
else:
    print(f'Car_1:___{car_1}')


try:
    car_2 = Car("Audi", 8888888, 7832)
except IncorrectVinNumber as v:
    print(f'ПЕРЕХВАТ ИСКЛЮЧЕНИЯ IncorrectVinNumber:  {v}')
except IncorrectCarNumbers as n:
    print(f'ПЕРЕХВАТ ИСКЛЮЧЕНИЯ IncorrectCarNumbers:  {n}')
else:
    print(f'Car_2:___{car_2}')

try:
    car_3 = Car("Skoda", 5555555, "MB9521")
except IncorrectVinNumber as v:
    print(f'ПЕРЕХВАТ ИСКЛЮЧЕНИЯ IncorrectVinNumber:  {v}')
except IncorrectCarNumbers as n:
    print(f'ПЕРЕХВАТ ИСКЛЮЧЕНИЯ IncorrectCarNumbers:  {n}')
else:
    print(f'Car_3:___{car_3}')


