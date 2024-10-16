print('\n')

'''Матрица воплоти.'''

def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        ma_x = [] # Создаём внутренний список.

        for j in range(m):
            if value > 0:
                ma_x.append(value) # Заполняем внутренний список.

        matrix.append(ma_x) # Вставляем внутренний список во внешний.

    return matrix


result_1 = get_matrix(2, 4, 71)
result_2 = get_matrix(3, 3, 47)
result_3 = get_matrix(3, 5, 58)

print(result_1)
print(result_2)
print(result_3)



