print('\n')

'''РАССЫЛКА ПИСЕМ.'''

def send_email(message, *, recipient, sender = "university.help@gmail.com"):

    if ("@" in sender)and("@" in recipient):

        if ".com" or ".ru" or ".net" in sender and recipietn:

            if sender == recipient:
                print('Невозможно отправить письмо самому себе!!!')
                return None

            elif sender == "university.help@gmail.com":
                print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient} !!!')
                return message

            else:
                print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!!! Письмо отправлено с адреса {sender} на адрес {recipient}...')
                return message

        else:
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient} !!!')
            return None

    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient} !!!')
        return None


'''ВЫЗОВЫ ФУНКЦИИ:'''

m = send_email('Hello, my friends!!! I send you a letter from nowhere to nowhere',
               recipient = "somethingland.net", sender = "nowhere@land")
print(f'Message: {m}\n')


m = send_email('Hello, nZmey!!! I sent a cool letter to myself!',
               recipient = "nzmey@gorod.net", sender = "nzmey@gorod.net")
print(f'Message: {m}\n')


m = send_email('Good Day, my friends!!! I miss you so!!!',
                recipient = "my_friend@goodday.ru", sender = "university.help@gmail.com")
print(f'Message: {m}\n')


m = send_email('Hello, the World!!! I welcome, my good World!!!',
               recipient =  "nzmey@good.net", sender = "world@good.com"    )
print(f'Message: {m}\n')





