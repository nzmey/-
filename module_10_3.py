print('\n')

'''   <<<  "Банковские операции.  >>>   '''

import threading
import random
import time

class Bank:

    count_lock = threading.Lock()
    balance = 0

    def deposit(self):
        for a in range(100):
            if self.count_lock.locked() and self.balance > 499:
                self.count_lock.release()
            # print(f'Блокировка СЧЁТА на депозите: {self.count_lock.locked()}\n')

            i = random.randint(50, 500)
            self.balance += i
            print(f'\nПополнение СЧЁТА на: {i} рублей. Баланс СЧЁТА: {self.balance} рублей.\n')
            time.sleep(0.05)

    def take(self):
        for a in range(100):
            d = random.randint(50, 500)
            print(f'Запрос на выделение средств со СЧЁТА в размере: {d} рублей.')
            if self.balance > d + 50:
                self.balance -= d
                print(f'Снятие со СЧЁТА в размере: {d}. Баланс СЧЁТА: {self.balance} рублей.\n')
            else:
                print(f'В запросе отказано. На балансе СЧЁТА не хватает средств.\n')
                self.count_lock.acquire()
                # print(f'Блокировка СЧЁТА при списании: {self.count_lock.locked()}\n')
            time.sleep(0.02)


bank = Bank()

thread_in = threading.Thread(target = bank.deposit)
thread_out = threading.Thread(target = bank.take)

thread_in.start()
thread_out.start()
thread_in.join()
thread_out.join()

print(f'\n\nБаланс СЧЁТА в БАНКЕ: {bank.balance}')







