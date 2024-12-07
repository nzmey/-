print('\n')

from time import sleep
from random import randint
from math import sqrt

'''УТКОНОС - ОШИБКА ЭВОЛЮЦИИ'''

class Animal:

    _coords = { 'dx':0, 'dy':0, 'dz':0 }

    def __init__(self, name, sound, speed  ):
        self.name = name
        self.sound = sound
        self.speed = speed
        '''Скорость движения по земле в м/с.'''

    def begin_coords(self):
        print('Я в заповеднике площадью 10 х 10 км. '
              'В начале координат - биостанция.')
        self._coords['dx'] = randint(1000, 9000)
        self._coords['dy'] = randint(1000, 9000)
        self._coords['dz'] = randint(0, 3)
        return ''

    def move(self):
        self.begin_coords()
        print('Я пошла...')
        cnt = 0
        vq = self.speed**2
        vxq = 0
        vyq = 0
        vzq = 0
        k = 0

        while cnt < 20:
            vzq = vq/10
            k = 1 - 2*(randint(1, 100)%2)
            self._coords['dz'] += int(sqrt(vzq)) * k
            if self._coords['dz'] > 3:
                self._coords['dz'] = int(3)
            if self._coords['dz'] < 0:
                self._coords['dz'] = int(0)
            if cnt > 15:
                self._coords['dz'] = int(0)

            vxq = ((vq - vzq)/10)*randint(1, 9)
            vyq = vq - vxq
            k = 1 - 2*(randint(1, 100)%2)
            self._coords['dx'] += int(sqrt(vxq)) * k
            k = 1 - 2*(randint(1, 100)%2)
            self._coords['dy'] += int(sqrt(vyq)) * k

            print('\r',
                  f'dx = {self._coords["dx"]}, '
                  f'dy = {self._coords["dy"]}, '
                  f'dz = {self._coords["dz"]}', end = '')

            vxq = 0
            vyq = 0
            vzq = 0
            k = 0
            sleep(1)
            cnt += 1
        return ''

    def attack(self):
        dd = self._DEGREE_OF_DANGER
        if dd < 5:
            print('Извините, Я - мирный!...')
        else:
            print('Будьте внимательны! А то, - Я вас укушу!!!...')

    def speak(self):
        print(f'Я - {self.name}. И говорю {self.sound}')



class Bird(Animal):

    def __init__(self, name, sound, speed, swings, beak):
        Animal.__init__(self,name, sound, speed)
        self.swings = swings
        self.beak = beak
        self.bird_speak()
        self.lay_eggs()

    def bird_speak(self):
        if self.swings:
            print('У меня есть КРЫЛЬЯ.')
        if self.beak:
            print('У меня есть КЛЮВ.')

    def fly_in(self):
        pass

    def lay_eggs(self):
        from random import randint
        n = randint(1, 5)
        if n == 1:
            print(f'Здесь {n} яйцо для тебя!...')
        else:
            print(f'Здесь {n} яйца для тебя!...')
        return ''

class AquaticAnimal(Animal):

    def __init__(self, name, sound, speed,  gills, flippers):
        Animal.__init__(self, name, sound, speed)
        self.gills = gills
        self.flippers = flippers
        self.aa_speak()

    def aa_speak(self):
        if self.gills:
            print('У меня есть ЖАБРЫ.')
        if self.flippers:
            print('У меня есть ЛАСТЫ.')

    def dive_in(self, speed_water):
        print('\nЯ поплыл...')
        '''Скорость в воде в м/с.'''
        cnt = 0
        vq = speed_water ** 2
        vxq = 0
        vyq = 0
        vzq = 0
        k = 0

        while cnt < 20:
            vzq = vq / 3
            k = 1 - 2 * (randint(1, 100) % 2)
            self._coords['dz'] += int(sqrt(vzq)) * k
            if self._coords['dz'] > 0:
                self._coords['dz'] = int(0)
            if cnt > 15:
                self._coords['dz'] = int(0)

            vxq = ((vq - vzq) / 10) * randint(1, 9)
            vyq = vq - vxq
            k = 1 - 2 * (randint(1, 100) % 2)
            self._coords['dx'] += int(sqrt(vxq)) * k
            k = 1 - 2 * (randint(1, 100) % 2)
            self._coords['dy'] += int(sqrt(vyq)) * k

            print('\r',
                  f'dx = {self._coords["dx"]}, '
                  f'dy = {self._coords["dy"]}, '
                  f'dz = {self._coords["dz"]}', end='')

            vxq = 0
            vyq = 0
            vzq = 0
            k = 0
            sleep(1)
            cnt += 1
        return ''


class PoisonousAnimal(Animal):

    def __init__(self, name, sound, speed, _DEGREE_OF_DANGER ):
        Animal.__init__(self, name, sound, speed)
        self._DEGREE_OF_DANGER = _DEGREE_OF_DANGER


class Duckbill(Bird, AquaticAnimal, PoisonousAnimal, Animal):


    def __init__(self, name = 'Duckbill', sound = "Click-click-click", speed = 8,
                 swings = False,  beak = True,
                 gills = False, flippers = True,
                 _DEGREE_OF_DANGER = 8):
        Bird.__init__(self, name, sound, speed, swings , beak)
        AquaticAnimal.__init__(self,name , sound, speed, gills , flippers )
        PoisonousAnimal.__init__(self, name, sound, speed, _DEGREE_OF_DANGER )
        self.speak()
        self.attack()
        self.move()
        self.dive_in(2)
        self.speak_end()

    def speak_end(self):
        print('\nЯ кого-то поймал и съел. Пойду спать. Всем СПОКОЙНОЙ НОЧИ!')


# print(Duckbill.mro())
an = Duckbill('Утконос БОБА', 'КРЯ-КРЯ-КРЯ!!!')


