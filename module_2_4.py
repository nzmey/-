print('\n')
'''Всё не так уж просто.'''

'''Исходные условия.'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

'''Создаём списки.'''
primes = []
not_primes = []

'''Проверяем, есть ли в списке "numbers" число ДВА... А оно есть!!!'''
for k in range(len(numbers)):
    if numbers[k] == 2:
        primes.append(numbers[k])
# Понимаю, что несколько ходульное решение... Но ДВОЙКА - единственное чётное простое число.
# И как его грамотно впихнуть в нужный список - пока не слишком понятно...

'''Сортируем числа.'''
d = 0
for i in range(2, len(numbers)):
    d = int(numbers[i]**0,5 + 1) 
   # Достаточно перебрать набор чисел, пределом которого будет корень из проверяемого числа, плюс единица.
    for j in range(2, d):
       if numbers[i] % j == 0:
            not_primes.append(numbers[i])
            break
   if numbers[i] not in not_primes:
        primes.append(numbers[i])

'''Выводим списки простых и непростых чисел.'''

print(f'Primes {primes}')
print(f'Not Primes{not_primes}')
