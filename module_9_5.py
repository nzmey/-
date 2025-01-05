print('\n')

'''   <<<  Range - это просто. >>>   '''

class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start
        if step == 0:
            raise StepValueError(print('Шаг не может быть равен НУЛЮ !!!'))

    def __iter__(self):
        return self

    def __next__(self):
        if self.pointer > self.stop and self.step > 0:
            raise StopIteration(print('\nИтерация окончена.'))
        elif self.pointer < self.stop and self.step < 0:
            raise StopIteration(print('\nИтерация окончена.'))
        else:
            res = self.pointer
            self.pointer += self.step
            return res

print('Iter_1:')
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно!!!')


iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

print('\nIter_2:')
for i in iter2:
    print(i, end=' ')

print('\nIter_3:')
for i in iter3:
    print(i, end=' ')

print('\nIter_4:')
for i in iter4:
    print(i, end=' ')

print('\nIter_5:')
for i in iter5:
    print(i, end=' ')




