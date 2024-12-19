print('\n')

'''   <<<  ФАЙЛЫ и их ХАРАКТЕРИСТИКИ.  >>>   '''

import os
import time

for root, dirs, files in os.walk("."):
    for i in files:
        file_name = i
        parent_dir = os.path.dirname(os.getcwd())
        file_path = os.getcwd()
        file_size = os.stat(i).st_size
        file_time_create = time.ctime(os.path.getctime(i))
        file_time_change = time.ctime(os.path.getctime(i))

        print(f'Файл: {file_name}')
        print(f'Родительские директории:  {parent_dir}')
        print(f'Путь: {file_path}')
        print(f'Размер: {file_size} кБ')
        print(f'Время создания: {file_time_create}')
        print(f'Время изменения: {file_time_change}')
        print('\n')

