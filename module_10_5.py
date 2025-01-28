print('\n')

'''   <<<  Многопроцессорное считывание.  >>>   '''

import multiprocessing, time, datetime, os

file_names_line = [f'file {number}.txt' for number in range(1, 5)]
file_names_process = [f'file {number}.txt' for number in range(1, 5)]

def read_info_line(name):
    all_data = []
    with open(name, "r", encoding = "UTF-8") as fl:
        ps = os.path.getsize(name)
        print(f'Размер файла <{name}> для Line функции = {ps}.')
        for _ in range(ps):
            s = fl.readline()
            all_data.append(s.strip())
            # if s == '':
            #     break
            # else:
            #     all_data.append(s.strip())
    print(f'Line функция: Файл <{name}>:')
    for i in range(5):
        print(all_data[i])
    # return all_data

# read_info_line("file 1.txt")

def read_info_process(name):
    all_data = []
    with open(name, "r", encoding = "UTF-8") as fl:
        ps = os.path.getsize(name)
        print(f'Размер файла <{name}> для Process функции = {ps}.')
        for _ in range(ps):
            s = fl.readline()
            all_data.append(s.strip())
            # if s == '':
            #     break
            # else:
            #     all_data.append(s.strip())
    print(f'Process функция: Файл <{name}>:')
    for i in range(5):
        print(all_data[i])
    # return all_data


if __name__ == '__main__':

    line_list = []

    begin_line = datetime.datetime.now()
    line_list += map(read_info_line, file_names_line)
    end_line = datetime.datetime.now()

    # for i in range(5):
    #     print(line_list[i])
    print(f'Время выполнения ЛИНЕЙНОГО считывания = {end_line - begin_line}.')

    # process_list = []

    begin_process = datetime.datetime.now()
    '''Создание пула из процессов - число которых будет определять функция "cpu_count()".'''
    with multiprocessing.Pool(processes = multiprocessing.cpu_count()) as pl:
    # with multiprocessing.Pool(processes = 4) as pl:
        res_p = pl.map(read_info_process, file_names_process)
    end_process = datetime.datetime.now()

    # begin_process = datetime.datetime.now()
    # for i in file_names_process:
    #     p_i = multiprocessing.Process(target = read_info_process, args = (i,))
    #     p_i.start()
    #     # p_i.join()
    # end_process = datetime.datetime.now()

    # for i in range(5):
    #     print(res[0][i])
    print(f'Время МУЛЬТИПРОЦЕССОРНОГО считывания = {end_process - begin_process}.')


'''
PS.
После запуска программы - результаты следующие:
Время выполнения ЛИНЕЙНОГО считывания = 0:25:46.602943.
Время МУЛЬТИПРОЦЕССОРНОГО считывания = 0:10:52.065537.

После того, как я установил для обеих функций 
выход из цикла считывания файла по пустой строке - 
- я получил следующие результаты:
Время выполнения ЛИНЕЙНОГО считывания = 0:00:14.024424.
Время МУЛЬТИПРОЦЕССОРНОГО считывания = 0:00:06.208811.

Число процессов - я отдал на откуп функции "cpu_count()"
 - ей виднее сколько процессов запускать.

'''




