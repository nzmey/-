print('\n')

'''Свой YouTube...'''

class Video:
    def __init__(self , title = 'КИНО' , duration = 60 , adult_mode = False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode

    def __str__(self):
        return str(f'"{title}", {duration}, {adult_mode}')

class User:

    def __init__(self, nickname ,password, birthday ):
        self.nickname = nickname
        self.password = password
        self.birthday = birthday

    def __str__(self):
        return str(f'"{nickname}", {password}, {birthday}')

''' <<<  ОСНОВНОЙ  РАБОЧИЙ  КЛАСС  >>> '''
class UrTube(Video, User):

    __users = {}
    __videos = {}

    '''КОНСТРУКТОР КЛАССА "UrTube" .'''
    __unique = None
    def __new__(cls):
        if cls.__unique == None:
            cls.__unique = super().__new__(cls)
        return cls.__unique

    '''Переворот ДАТЫ.'''
    def __turn_date(self, date):
        str_1 = ''
        str_2 = ''
        str_3 = ''
        cnt = 0
        for i in date:
            if i == '.':
                cnt += 1
                continue
            if cnt == 0:
                str_1 += i
            elif cnt == 1:
                str_2 += i
            else:
                str_3 += i
        res_date = str_3 + str_2 + str_1
        return res_date


    '''  ВИДЕО  >>>  ВИДЕО  >>>  ВИДЕО  >>>  ВИДЕО  >>>  ВИДЕО  >>>  ВИДЕО  '''

    '''Добавление БАЗЫ ВИДЕО: '''
    def __add_video_base(self, *arg):
       f_list = []
       for i in arg:
           f_list.append(i.duration)
           f_list.append(i.adult_mode)
           self.__videos[i.title] = f_list
           f_list = []

    '''Индивидуальное добавление ВИДЕО.'''
    def __add_video_unique(self):
        f_list = []
        choice = None
        print('Добавление нового ВИДЕО:')
        while True:
            print('Введите НАЗВАНИЕ видео:')
            title = input('  __  ')
            if title in self.__videos:
                print('Такое видео уже существует в БАЗЕ!!!\n'
                      'Хотите добавить ДРУГОЕ ВИДЕО? - ДА или НЕТ?')
                choice = input('  __  ').upper()
                if choice == 'ДА':
                    continue
                else:
                    return ''
            else:
                print('Введите ВРЕМЯ ПРОСМОТРА.')
                duration = input('  __  ')
                f_list.append(duration)
                print('18+ ? - ДА или НЕТ...')
                adult_mode = input('  __  ').upper()
                if adult_mode == 'ДА':
                    f_list.append(True)
                else:
                    f_list.append(False)
                self.__videos[title] = f_list
                print(f'ВИДЕО {title} - успешно добавлено в БАЗУ .')
                print('Показать БАЗУ ?')
                self.__show_videos()
            print('Хотите ещё добавить ВИДЕО в БАЗУ? - ДА или НЕТ?')
            choice = input('  __  ').upper()
            if choice == 'ДА':
                continue
            else:
                choice = None
                return ''

    '''Удаление ВИДЕО.'''
    def __video_delete(self):
        print('УДАЛЕНИЕ ВИДЕО:')
        while True:
            print('Введите название ВИДЕО, которое вы хотите удалить из БАЗЫ.')
            title = input('  __  ')
            if title in self.__videos:
                video = self.__videos.pop(title)
                print(f'ВИДЕО {title} успешно удалено.')
                print('Смотрите БАЗУ ВИДЕО:\n')
                self.__show_videos()
                return video
            else:
                print('...!!!...Такого ВИДЕО в БАЗЕ НЕТ...!!!...')
            print('Хотите удалить ещё какое-нибудь ВИДЕО из БАЗЫ? - ДА или НЕТ?')
            choice = input('  __  ').upper()
            if choice == 'ДА':
                continue
            else:
                return None

    '''Просмотр БАЗЫ ВИДЕО...для админов...'''
    def __show_videos(self):
        print('\nБАЗА ВИДЕО:\n')
        for key, value in self.__videos.items():
            print(f'Title: {key},\t\t  Properties: {value}')

    '''Просмотр БАЗЫ ВИДЕО...для пользователей...'''
    def __show_video_user(self):
        u_list = []
        raw_list = self.__videos.keys()
        u_list = sorted(raw_list)
        for i in u_list:
            if self.__videos[i][1] == True:
                print(f'{i}(18+)')
            else:
                print(i)


    '''  ПОЛЬЗОВАТЕЛИ  >>>  ПОЛЬЗОВАТЕЛИ  >>>  ПОЛЬЗОВАТЕЛИ  >>>  ПОЛЬЗОВАТЕЛИ  '''

    '''Добавление БАЗЫ ПОЛЬЗОВАТЕЛЕЙ: '''
    def __register_user_base(self, *arg):
        f_list = []
        for i in arg:
            f_list.append(i.password)
            f_list.append(i.birthday)
            self.__users[i.nickname] = f_list
            f_list = []

    '''Просмотр БАЗЫ ПОЛЬЗОВАТЕТЕЙ... для админов...'''
    def __show_users(self):
        print('\nБАЗА ПОЛЬЗОВАТЕЛЕЙ:\n')
        for key, value in self.__users.items():
            print(f'Name: {key},\t\t Pass Word and Birthday: {value}')

    '''Индивидуальная РЕГИСТРАЦИЯ ПОЛЬЗОВАТЕЛЕЙ.'''
    def __register_user_unique(self):
        print('Регистрация нового пользователя:')
        print('Введите СВОЙ NICKNAME:')
        cnt = 0
        while True:
            cnt += 1
            nickname = input('  __  ')
            if nickname in self.__users:
                if cnt < 4:
                    print('Такой NICKNAME уже есть в БАЗЕ.\n'
                          'Придумайте что-нибудь другое! ')
                else:
                    print('Ну, не судьба вам сегодня к нам попасть...\n'
                          'Попытайтесь в следующий раз....\n'
                          'ДО ВСТРЕЧИ!!!')
                    exit()
            else:
                break
        print('Введите свой ДЕНЬ РОЖДЕНИЯ: "хх.хх.хххх" ...')
        bd = input('  __  ')
        f_list = []
        cnt = 0
        while True:
            print('Введите ПАРОЛЬ: "ххх" ...')
            pw = int(input('  __  '))
            print('Повторите ПАРОЛЬ: "ххх" ...')
            r_pw = int(input('  __  '))
            if pw == r_pw:
                f_list.append(pw)
                f_list.append(bd)
                self.__users[nickname] = f_list
                break
            else:
                cnt +=1
                if cnt < 4:
                    print('Ваши ПАРОЛИ не совпадают!\n'
                          'ВВЕДИТЕ ИХ ЗАНОВО!!!')
                    continue
                else:
                    print('Так больше не возможно...\n'
                          'Зарегистрируетесь в другой раз...')
                    exit()


    '''Удаление ПОЛЬЗОВАТЕЛЯ.'''
    def __user_delete(self):
        print('УДАЛЕНИЕ ПОЛЬЗОВАТЕЛЯ:')
        while True:
            print('Введите NICKNAME ПОЛЬЗОВАТЕЛЯ,\n'
                  'которого вы хотите удалить из БАЗЫ.')
            name = input('  __  ')
            if name in self.__users:
                user = self.__users.pop(name)
                print(f'Пользователь {name} успешно удалён.')
                print('Смотрите БАЗУ ПОЛЬЗОВАТЕЛЕЙ:\n')
                self.__show_users()
                return user
            else:
                print('...!!!...Такого ПОЛЬЗОВАТЕЛЯ в БАЗЕ НЕТ...!!!...')
            print('Хотите удалить ещё кого-нибудь из БАЗЫ? - ДА или НЕТ?')
            choice = input('  __  ').upper()
            if choice == 'ДА':
                continue
            else:
                return None


    '''  <<<   <<<   ГЛАВНАЯ   ВХОДНАЯ   ФУНКЦИЯ   КЛАССА   >>>   >>>  '''

    def get_video(self):
        from time import strftime
        c_date = strftime('%d.%m.%Y') # Функция текущего времени.
        print(' """ ЗДРАВСТВУЙТЕ !!! """ ')
        print(f'Сегодня: __ {c_date}')
        print('Войдите в аккаунт или зарегистрируйтесь:')
        print('Войти - 0. Зарегистрироваться - ЛЮБОЕ ЧИСЛО:')
        choice = int(input('  __  '))
        if choice:
            self.__register_user_unique()
            print('Спасибо!!! Вы успешно зарегистрировались!\n'
                  'Теперь войдите в свой аккаунт. И для начала...')
        bd = self.__login_user()
        self.__find_video(bd, c_date)
        print('\n\nСПАСИБО ЗА ВНИМАНИЕ! ДО СВИДАНИЯ!\n\n')

    '''Пользовательский ВХОД...'''
    def __login_user(self):
        name = None
        cnt_1 = 0
        cnt_2 = 0
        choice = None
        print('\n <<< ВХОД В НАШ С ВАМИ ОБЩИЙ YOU TUBE >>>\n')
        while True:
            print('Введите ИМЯ:')
            name = input('  __  ')
            if name in self.__users:
                while True:
                    print('Введите ПАРОЛЬ:')
                    pw = int(input('  __  '))
                    if pw == self.__users[name][0]:
                        print('ВХОД ВЫПОЛНЕН!!! Ура!!!\n\n')
                        return self.__users[name][1] # Возвращает ДАТУ рождения.
                    else:
                        cnt_1 += 1
                        if (cnt_1 < 3) and (cnt_1 != 4):
                            print('Неверный ПАРОЛЬ!!! Повторите ВВОД ПАРОЛЯ.')
                            continue
                        elif cnt_1 == 3:
                            print(f'Ну ЧТО, {name}, забыли ПАРОЛЬ ?'
                                  f'Показать БАЗУ?...')
                            choice = input('  __  ').upper()
                            if choice == 'ДА':
                                self.__show_users()
                            else:
                                choice = None
                            continue
                        elif cnt_1 > 4:
                            print('Нет... Видно, сегодня - не судьба...'
                                  'Приходите как-нибудь ещё раз...')
                            exit()
            else:
                cnt_2 += 1
                if (cnt_2 < 3) and (cnt_2 != 3):
                    print('Такого имени НЕТ! Повторите ВВОД ИМЕНИ.')
                    continue
                elif cnt_2 == 3:
                    print('Вы уже ПЯТЫЙ раз пытаетесь ввести своё собственное ИМЯ!!!\n'
                          'ВЫ ЧТО?!... ВЫПИЛИ???  !!!...')
                    continue
                elif cnt_2 > 4:
                    print('ИДИТЕ к ЧЁРТУ!!!\n'
                          'Вначеле протрезвейте... потом поговорим...')
                    exit()

    '''Поиск ВИДЕО...'''
    def __find_video(self, birthday, current_day):
        print('Что хотите посмотреть?\n\n')
        self.__show_video_user()
        while True:
            print('\nВведите название ВИДЕО:')
            ch_v = input('  __  ')
            if ch_v in self.__videos:
                print('...УРА! - ВИДЕО НАШЛОСЬ!!!...\n')

                age = int((int(self.__turn_date(current_day)) -
                           int(self.__turn_date(birthday))) / 10000)
                if age < 18 and self.__videos[ch_v][1] == True :
                    print('... но... Вам отказано по возрасту...')
                    print('Хотите ещё что-нибудь?... ДА или НЕТ?...')
                    ch_u = input('  __  ').upper()
                    if ch_u == 'ДА':
                        continue
                    else:
                        break
                else:
                    print('\nСМОТРИТЕ ВИДЕО!!!...\n')
                    self.__watch_video(ch_v, self.__videos[ch_v][0])
            else:
                print('Такого видео у нас нет...')
            print('Хотите что-нибудь ещё посмотреть?... ДА или НЕТ?...')
            ch_u = input('  __  ').upper()
            if ch_u == 'ДА':
                continue
            else:
                break

    '''Просмотр ВИДЕО...'''
    def __watch_video(self, name = 'КИНО', v_time = 300):
        from time import sleep
        f_time = int(v_time / 10)
        print(f'\n <<<  <<<   {name}  >>>  >>> \n')
        for i in range(f_time):
            sleep(1)
            print('\r',f'{(i+1)}0','минута',end='')
        print('\n...КОНЕЦ...')


'''ОБЪЯВЛЯЕМ ГЛАВНЫЙ И ЕДИНСТВЕННЫЙ ОБЪЕКТ КЛАССА "UrTube" !!!'''
ut = UrTube()

'''ВИДЕО:...'''
v_1 = Video('Программа ВРЕМЯ... реальное...ужасы...///', 300, True)
v_2 = Video('Секс за компом...этотическая драма...///', 200, False)
v_3 = Video('Секс без компа...комедия...///', 60, False)
v_4 = Video('Ужасы ночных кошмаров...комедия...///', 180, False)
v_5 = Video('Кошмары ночных ужасов...ужасы...///', 200, True)
v_6 = Video('Весёлая РОБОТОТЕХНИКА...комедия...///', 80, False)
v_7 = Video('Грустная робототехника...драма...///', 120, True)
v_8 = Video('КОШМАРНАЯ РОБОТОТЕХНИКА...ужасы...///', 180, True)
v_9 = Video('Кошмарные ужасы...комедия...///', 120, False)
v_10 = Video('Ужасные кошмары...мультики...///', 90, False)
v_11 = Video('КОД, пропавший вместе с КОТОМ...детектив...///', 90, False)
v_12 = Video('Исчезающий ХОЛОДИЛЬНИК... ужасы...///', 120, True)
v_13 = Video('Раздумья УМНОГО ДОМА... драма...///', 350, False)
v_14 = Video('ВЕСЁЛЫЕ БРЫЗГИ... мультики...///', 60, False)
v_15 = Video('Комьютерный СМЕХ...ужасы для детей...///', 80, False)
v_16 = Video('Игры КОМЬЮТЕРНОГО РАЗУМА...драма...', 180, True)
v_17 = Video('Компьютерные КУПЛЕТЫ...короткометражка...///', 40, False)
v_18 = Video('Компьютерные ВОЙНЫ...мультики...///', 80, False)
v_19 = Video('ВЕСЁЛЫЕ КОМПЫ...ужасы...///', 120, True)
v_20 = Video('Заводное ПИАНИНО...комедия...///', 90, False)
v_ = Video('', 60, False)
# v_ = Video('', 60, False)

'''Административный доступ к БАЗЕ ВИДЕО. Загрузка БАЗЫ.'''
ut._UrTube__add_video_base(v_1, v_2, v_3, v_4, v_5,
                  v_6, v_7, v_8, v_9, v_10,
                  v_11, v_12, v_13, v_14, v_15,
                  v_16, v_17, v_18, v_19, v_20)

'''Просмотр БАЗЫ ВИДЕО... для админов...'''
# ut._UrTube__show_videos()

print('\n============================================================================\n')

'''ЮЗЕРЫ:...'''
us_1 = User('Den', 123, '23.10.2010')
us_2 = User('Max', 234, '12.08.2011')
us_3 = User('Mary', 789, '18.03.2015')
us_4 = User('Cat', 456, '28.03.2010')
us_5 = User('Catty', 654, '16.09.2009')
us_6 = User('Bob', 987, '15.05.2003')
us_7 = User('Nick', 345, '22.02.2007')
us_8 = User('Sia', 543, '26.04.2012')
us_9 = User('Victor', 321, '05.12.2005')
us_10 = User('Suzi', 890, '08.09.2011')
us_11 = User('Pau', 678, '14.06.2013')
us_12 = User('Victoria', 876, '25.07.2004')
us_13 = User('Linda', 765, '28.08.2013')
us_14 = User('Sony', 123, '15.03.2007')
us_15 = User('Give', 321, '24.10.2005')
us_ = User('', 123, '')
# us_ = User('', 123, '')

'''Административный доступ к БАЗЕ ПОЛЬЗОВАТЕЛЕЙ. Загрузка БАЗЫ.'''
ut._UrTube__register_user_base(us_1, us_2, us_3, us_4, us_5,
                      us_6, us_7, us_8, us_9, us_10,
                      us_11, us_12, us_13, us_14, us_15)
'''Просмотр БАЗЫ ПОЛЬЗОВАТЕЛЕЙ... для админов...'''
# ut._UrTube__show_users()

'''///////////////////////////////////////////////////////////////////////////////'''



''' <<<   ГЛАВНАЯ   ВХОДНАЯ   ФУНКЦИЯ   КЛАССА   >>> '''
ut.get_video()



'''///////////////////////////////////////////////////////////////////////////////'''

print('\n============================================================================\n')

print('\n <<<  АДМИНИСТРАТИВНАЯ  ЧАСТЬ  ПРОЕКТА  >>> \n')

'''Просмотр БАЗЫ ВИДЕО... для админов...'''
ut._UrTube__show_videos()

'''Просмотр БАЗЫ ПОЛЬЗОВАТЕЛЕЙ... для админов...'''
ut._UrTube__show_users()


'''ДОБАВЛЕНИЕ НОВОГО ВИДЕО В БАЗУ - вначале ЗАПИШИТЕ ВСЁ ЗДЕСЬ !!!...'''
'''... чтобы потом не потерять ВАШЕ ВИДЕО...

Например:
Программа ищет, но не спасает...детектив.../// , 120, False
Секс под компом...комедия.../// , 120 , False
 
'''
print('\n\nХотите добавить новое ВИДЕО в БАЗУ? ...да или что-нибудь...?')
choice = input('  __  ').upper()
if choice == 'ДА':
    ut._UrTube__add_video_unique()
else:
    print('Ну, как хотите...\n')

print('\n\nХотите удалить какое-нибудь ВИДЕО из БАЗЫ? ...да или что-нибудь...?')
choice = input('  __  ').upper()
if choice == 'ДА':
    ut._UrTube__video_delete()
else:
    print('Ну, как хотите...\n')

print('\n============================================================================\n')

'''РЕГИСТРАЦИЯ НОВОГО ПОЛЬЗОВАТЕЛЯ - вначале ЗАПИШИТЕ ВСЁ ЗДЕСЬ !!!...'''
'''... чтобы потом НЕ ПОТЕРЯТЬСЯ !!!...

Например:
"Маша_Простокваша" , 512, '12.08.2003'
"Лучик_Света" , 543 , '24.03.2012'

'''
print('\n\nХотите добавить нового ПОЛЬЗОВАТЕЛЯ в БАЗУ? ...да или что-нибудь...?')
choice = input('  __  ').upper()
if choice == 'ДА':
    ut._UrTube__register_user_unique()
    ut._UrTube__show_users()
else:
    print('Ну, как хотите...\n')

print('\n\nХотите удалить какого-нибудь ПОЛЬЗОВАТЕЛЯ из БАЗЫ? ...да или что-нибудь...?')
choice = input('  __  ').upper()
if choice == 'ДА':
    ut._UrTube__user_delete()
else:
    print('Ну, как хотите...\n')


''' <<< PS >>> '''
'''Почему мне грустно... Дело в том, что - насколько я понимаю,
Python - является "ЯЗЫКОМ СТРОКИ". 
Если "С++" - является языком ЦЕЛЫХ ЧИСЕЛ, или - по крайней мере
стремится таковым быть, ... - то Python - это СТРОКА...
СТРОКА - это его, пожалуй, главный связующий элемент между объектами...
Да и объекты его - порой, так и стремятся превратиться в строку...
Строку на английском языке, - с которым у меня - пока - очень плохо...
Но, надеюсь, со временем - станет лучше...
Что делать... Я, порой, сам не против написать что-нибудь витиеватое...
Например, - выразить некую техническую идею - максимально "художественным" языком.
Вот я иногда и подумываю, ... - а что, если как-нибудь - соорудить РУССКИЙ АНАЛОГ Питона...
Где будет главенствовать СТРОКА РУССКОГО ЛИТЕРАТУРНОГО ЯЗЫКА - во всей его
величиватости и могучевости...
Ну, скажите, наконец, - не это ли будет ВЕЛИКИМ СЛИЯНИЕМ физики и лирики, -
о котором так долго мечтали и говорили... да кто, только вообще об этом
хотя бы раз в жизни не заикнулся...
Никто и представить себе не может, - что будет, - когда всею своею обрушительной мощью -
на стройные ряды точных наук - нахлынет вал гуманитарного эстетизма...
Страшно подумать, - какие отдалённые горизонты замаячат на отдалённых отголосках
нашего сознания...
Хотя, - если бы мне - когда-нибудь выпала бы возможность заниматься сочинением
нового программистического языка - то для начала - я бы придумал предельно чёткий,
предельно простой и логичный скелет на целых числах... Да уж что говорить...
Скатился бы куда-нибудь в ассемблер... или ещё куда пониже... как Линус Торвальдс...
Только ничего не подумайте... К завязке сандали этого гения притронуться я не достоин...
Да... грустно, господа... грустно...
Интересно, а что ВЫ об этом думаете?...
'''





