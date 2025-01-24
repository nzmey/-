print('\n')

'''   <<<  Многопроцессорное считывание.  >>>   '''

import multiprocessing, time, datetime

file_names_line = [f'./file {number}.txt' for number in range(1, 5)]
file_names_process = [f'./file {number}.txt' for number in range(1, 5)]


def read_info_line(name):
    all_data = []
    with open(name, "r", encoding = "UTF-8") as fl:
        for _ in fl:
            s = fl.readline()
            # print(s)
            if s == '':
                break
            else:
                all_data.append(s.strip())
            # time.sleep(0.5)
    # print(all_data)
    return all_data

# read_info_line("file 1.txt")

def read_info_process(name):
    all_data = []
    with open(name, "r", encoding = "UTF-8") as fl:
        for _ in fl:
            s = fl.readline()
            # print(s)
            if s == '':
                break
            else:
                all_data.append(s.strip())
            # time.sleep(0.5)
    # print(all_data)
    return all_data


if __name__ == '__main__':

    line_list = []

    begin_line = datetime.datetime.now()
    line_list += list(map(read_info_line, file_names_line))[0]
    end_line = datetime.datetime.now()

    for i in range(10):
        print(line_list[i])
    print(f'Время выполнения ЛИНЕЙНОГО считывания = {end_line - begin_line}.')

    process_list = []

    begin_process = datetime.datetime.now()
    '''Создание пула из процессов - число которых будет определять функция "cpu_count()".'''
    with multiprocessing.Pool(processes = multiprocessing.cpu_count()) as pl:
        res = pl.map(read_info_process, file_names_process)
        process_list += list(res)[0]
    end_process = datetime.datetime.now()


    for i in range(10):
        print(process_list[i])

    print(f'Время МУЛЬТИПРОЦЕССОРНОГО считывания = {end_process - begin_process}.')


'''
PS.
Результаты следующие:
Время выполнения ЛИНЕЙНОГО считывания = 0:00:08.199469.
Время МУЛЬТИПРОЦЕССОРНОГО считывания = 0:00:10.683611.
Или - около того.

В моём компе - всего ДВА физических ядра и ЧЕТЫРЕ виртуальных.
Очевидно - именно поэтому - ЛИНЕЙНОЕ считывание 
происходит быстрее МУЛЬТИПРОЦЕССОРНОГО считывания.
Число процессов - я отдал на откуп функции "cpu_count()"
 - ей виднее сколько процессов запускать.

Функции считывают файлы - намного быстрее, чем предполагалось в задании.
Там линейная версия считывает файлы аж за целых ТРИ с лишним минуты.
У меня тоже такое было, - пока я не запретил считывание пустых строк.

При всём при этом - вынужден был обеспечить возврат списка 
в каждой из считывающих функций. Иначе - не работает.
'''







