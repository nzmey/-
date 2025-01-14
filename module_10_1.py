print('\n')


import threading
import time


'''   <<<   Потоковая запись в файлы.   >>>   '''


with open("example_1.txt", "w", encoding = "utf-8") as fl:
    fl.write('')
with open("example_2.txt", "w", encoding = "utf-8") as fl:
    fl.write('')
with open("example_3.txt", "w", encoding = "utf-8") as fl:
    fl.write('')
with open("example_4.txt", "w", encoding = "utf-8") as fl:
    fl.write('')
with open("example_5.txt", "w", encoding = "utf-8") as fl:
    fl.write('')
with open("example_6.txt", "w", encoding = "utf-8") as fl:
    fl.write('')
with open("example_7.txt", "w", encoding = "utf-8") as fl:
    fl.write('')
with open("example_8.txt", "w", encoding = "utf-8") as fl:
    fl.write('')


def wite_words(word_count, file_name):
    cnt = 0
    with open(file_name, "w", encoding = "utf-8") as f_fl:
        begin = time.time()
        for n in range(word_count):
            f_fl.write(f"Какое-то слово №: <{cnt}>")
            cnt += 1
            time.sleep(0.1)
        end = time.time()
    print(f"Завершилась запись в файл <{file_name}>")
    print(f'Время выполнения кода: {end - begin} сек.\n')



thread_1 = threading.Thread(target = wite_words, args = (10, "example_5.txt"))
thread_1.start()
thread_1.join()

thread_2 = threading.Thread(target = wite_words, args = (30, "example_6.txt"))
thread_2.start()
# thread_2.join()

thread_3 = threading.Thread(target = wite_words, args = (200, "example_7.txt"))
thread_3.start()
# thread_3.join()

thread_4 = threading.Thread(target = wite_words, args = (100, "example_8.txt"))
thread_4.start()
# thread_4.join()

wite_words(10, "example_1.txt")
wite_words(30, "example_2.txt")
wite_words(200, "example_3.txt")
wite_words(100, "example_4.txt")





