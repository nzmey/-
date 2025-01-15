print('\n')

'''   <<<  За честь и отвагу!  >>>   '''

import threading
import time
import random

class Knight(threading.Thread):
    def __init__(self, name, day_lengths):
        threading.Thread.__init__(self)
        self.name = name
        self._day_lengths = day_lengths

    def run(self):
        print(f'\n\n{self.name} принял бой с демонами!\n\n')

        number_of_daemons = 100
        cnt = 1
        power = 1
        while number_of_daemons > 0:
            power = random.randint(7, 11)
            if number_of_daemons > power:
                print(f'В {cnt} день битвы - {self.name} одолел {power} демонов.')
            else:
                print(f'В {cnt} день битвы - {self.name} одолел всех оставшихся демонов.')
            number_of_daemons -= power
            if number_of_daemons > 0:
                print(f'Демонов осталось {number_of_daemons} и {self.name} их победит.\n')
            else:
                print(f'Больше демонов не осталось!!! {self.name} всех победил!\n')
            time.sleep(self._day_lengths)
            cnt +=1

        print(f'ИТОГ БИТВЫ: {self.name} победил всех демонов!\n')

thread_A = Knight(name = "Принц АРДЖУНА", day_lengths = 3.2)
thread_B = Knight(name = "Рыцарь БЕОВУЛЬФ", day_lengths = 2.7)

thread_A.start()
thread_B.start()

# thread_A.join(4)
# thread_B.join()






