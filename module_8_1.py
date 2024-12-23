print('\n')


'''   <<<   ПРОГРАММИСТАМ МОЖНО ВСЁ!!!  >>>   '''


def add_everything_up(a, b):
    result = 0
    try:
        result = a + b
    except TypeError as exc:

        if isinstance(a, str):
            print(F'\nИСКЛЮЧЕНИЕ: {exc}: Складываем строки:')
            result = a + ' ' + str(b)
        if isinstance(a, (int, float)):
            print(F'\nИСКЛЮЧЕНИЕ: {exc}: Складываем числа:')
            result = a + len(b)
    else:
        if isinstance(a, str) and isinstance(b, str):
            print('\nСкладываем строки:')
            result = a + ' ' + b
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            print('\nСкладываем числа:')

            result = a + b
    finally:
        print(f"Result = {result}")
        result = 0

add_everything_up(34, 28.34)
add_everything_up(34.121, 75)
add_everything_up(34, 'cat')
add_everything_up('white', 'cat')
add_everything_up('cat', 42)






















