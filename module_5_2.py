print('\n')

'''МАГИЧЕСКИЕ ЗДАНИЯ... продолжаем строить...'''

class House:
    def __init__(self, name = 'House', number_of_floors = 1, liver = 'Den'):
        self.name = name
        self.number_of_floors = number_of_floors
        self.liver = 'Den'

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Наша контора называется {self.name}, а этажей в ней {self.number_of_floors}.'

    def go_to(self, new_floor=1):
        if 0 < new_floor < self.number_of_floors+1:
            for i in range(1, new_floor+1):
                print(f'Этаж № {i}')
            print('Мы приехали!!!\n')
        else:
            print("Такого этажа не существует!!!\n")

house = House()
print(house)
print('Так сколько у нас этажей?... Правлильно!!!')
print(len(house))

print('\nВызываем несуществующий лифт без этажа - по умолчанию:')
house.go_to()
floor = 24
print(f'Вызываем тот же лифт на {floor} этаж:')
house.go_to(floor)
print(f'Хозяин кооператива "{house.name}" - {house.liver} - '
      f'благодарит нас и вас за посещение!...\n')

print('\n==========================================================================\n')

house_by_river = House('Дом на набережной', 23)
print(house_by_river)
print('Так сколько у нас этажей?... Правлильно!!!')
print(len(house_by_river))

floor = 12
print(f'\nВызываем лифт на {floor} этаж:')
house_by_river.go_to(floor)
floor = 29
print(f'Вызываем лифт на {floor} этаж:')
house_by_river.go_to(floor)

print(f'Хозяин кооператива "{house_by_river.name}" - {house_by_river.liver} - '
      f'благодарит нас и вас за посещение!...\n')