print('\n')

'''   <<< Потоки гостей в кафе.  >>>    '''

import threading
import queue
import time
import random


class Table:

    def __init__(self, number, guest = None):
        self._number = number
        self._guest = guest


class  Guest(threading.Thread):

    def __init__(self, name, eat_num = 0):
        threading.Thread.__init__(self)
        self._name = name
        self._eat_num = eat_num

    def run(self):
        t = random.randint(3, 10)
        time.sleep(t)


class Cafe:

    queue_cafe = queue.Queue()

    def __init__(self, *tables ):
        self._tables = tables

    def guest_arrival(self, *guests):

        print('\nКафе \n"АЙ, КАК ВКУСНО!!!" - \nОТКРЫВАЕТСЯ!!!'
              '\nУРА!!!... Налетай - торопись!!!...')
        time.sleep(3)

        cnt_tb = 0
        i_tb = 0
        i_gst_list = []

        while cnt_tb < len(self._tables):
            i_tb = random.randint(0, len(self._tables)-1)
            i_gst = random.randint(0, len(guests)-1)
            if self._tables[i_tb]._guest == None and i_gst not in i_gst_list:

                self._tables[i_tb]._guest = guests[i_gst]

                if not self._tables[i_tb]._guest.is_alive():
                    self._tables[i_tb]._guest.start()
                else:
                    new_guest = Guest(name = guests[i_gst]._name)
                    print('ОШИБКА!!!')

                    self._tables[i_tb]._guest = None
                    self._tables[i_tb]._guest = new_guest
                    self._tables[i_tb]._guest.start()

                i_gst_list.append(i_gst)
                cnt_tb += 1

                if self._tables[i_tb]._guest.is_alive():
                    print(f'\nГость {guests[i_gst].name} занял(а) стол № '
                          f'{self._tables[i_tb]._number}.')

            else:
                continue
            time.sleep(0.5)

        return i_gst_list


    def sending_queue(self, *guests, g_out):

        for i in range(len(guests)):
            if i not in g_out:
                self.queue_cafe.put(guests[i])
                print(f'\nГость {guests[i].name} отправлен(а) в очередь.')
            else:
                continue
            time.sleep(0.5)


    def serving_guests(self, lim_patience):

        t_counter = 0
        last_words = 0
        cnt_none = 0

        while True:
            for j in range(len(self._tables)):
                time.sleep(0.5)

                if self._tables[j]._guest is not None:
                    cnt_none = 0

                    if self._tables[j]._guest.is_alive():
                        continue

                    if not self._tables[j]._guest.is_alive():
                        self._tables[j]._guest._eat_num += 1
                        print(f'\nГость {self._tables[j]._guest._name} уже поел(а) '
                              f'за столом № {self._tables[j]._number} '
                              f'в свой {self._tables[j]._guest._eat_num}-й раз и ушёл... '
                              f'(или ушла)... не попращавшись... ')

                        # print(self._tables[j]._guest.is_alive())

                        if t_counter < lim_patience:
                            print('Ох!... Видимо - опять в очередь...')

                            new_guest = Guest(name = self._tables[j]._guest._name,
                                              eat_num = self._tables[j]._guest._eat_num)

                            self.queue_cafe.put(new_guest)

                            t_counter += 1
                            # print(f't_counter = {t_counter}')

                        else:
                            print('Похоже... теперь уже навсегда...')

                            if last_words == 0:
                                print('\n<...потому что ...всякому терпению приходит предел... '
                                      '\nСколько можно жрать?!!!...>'
                                      '\nКафе ЗАКРЫВАЕТСЯ!!!'
                                      '\nВ очередь не становиться!!!'
                                      '\nРаботаем до полседнего посететеля!!!')
                                last_words = 1
                                time.sleep(3)

                        if not self.queue_cafe.empty():
                            gst = self.queue_cafe.get()
                            self._tables[j]._guest = gst
                            self._tables[j]._guest.start()
                            if self._tables[j]._guest.is_alive():
                                print(f'\nГость {gst._name} занял(а) стол № '
                                      f'{self._tables[j]._number}.')
                        else:
                            # self._tables[j]._guest.__del__()
                            self._tables[j]._guest = None
                            continue

                elif self._tables[j]._guest is None:
                    cnt_none += 1
                    # print(f'cnt_none = {cnt_none}')
                    if cnt_none < 21:
                        continue
                    else:
                        # print('cnt_none None')
                        break

            if cnt_none > 20:
                # print('cnt_none while')
                break


# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
s_q = cafe.guest_arrival(*guests)

# Отправка гостей в очередь
cafe.sending_queue( *guests, g_out = s_q)

# Обслуживание гостей - НЕВЕРНО!!! Следует написать cafe.serving_guests()
# cafe.discuss_guests()
cafe.serving_guests(lim_patience = 30)

'''
PS. В тексте домашнего задания - в названии последней функции - допущена ошибка.
Вместо "discuss_guests" - ДИСКУССИЯ ГОСТЕЙ - следует написать "serving_guests" -
- ОБСЛУЖИВАНИЕ ГОСТЕЙ.
'''


