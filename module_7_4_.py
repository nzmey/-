print('\n')


'''   <<<  ФОРМАТИРОВАНИЕ СТРОК.  >>>   '''


print('\n   <<<  Использоварие ЗНАКА "%"  >>>\n')

print('В команде Мастера кода участников: %(team1_num)d !'%{'team1_num':5})
print('Итого сегодня в командах участников: %(team1_num)d и %(team2_num)d !'%{'team1_num':5, 'team2_num':6})



print('\n  <<<  Использование ОПЕРАТОРА "format"  >>>   \n')

print('Команда Волшебники данных решила задач: {score_2} !'.format(score_2 = 42))
print('Волшебники данных решили задачи за {team1_time} с !'.format(team1_time = 18015.2))


print('\n   <<<  Использование "f-СТРОКИ"  >>>   \n')

score_1 = 40
score_2= 42
print(f'Команды решили {score_1} и {score_2} задач')
challenge_result = 'Мастера кода'
print(f'Результат битвы: победа команды {challenge_result} !')
tasks_total = 82
time_avg = 350.4
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')



