print('\n')

'''  <<<  "Учёт товаров" >>>  '''
class Product:

    def __init__(self, name, weight, category):
        self.name = name
        '''Вес товара в килограммах.'''
        self.weight = weight
        self.category = category
        self.__str__()

    def __str__(self):
        return str(f'{self.name}, {self.weight}, {self.category}')

class Shop:

    __file_name = 'products.txt'
    comon = open(__file_name, 'a')
    comon.write('')
    comon.close()

    def get_products(self):
        content = open(self.__file_name, 'r')
        print(content.read())
        content.close()

    def add(self, *products):
        f_list = []
        f_list.append(products)
        comon = open(self.__file_name, 'r')
        s = comon.read()
        comon.close()

        for i in products:
            comon = open(self.__file_name, 'r')
            s = comon.read()
            comon.close()
            if str(i) in s:
                print(f'{i} - Такой товар уже имеется.')
                continue
            else:
                text = open(self.__file_name, 'a')
                text.write(str(i))
                text.write('\n')
                text.close()


print('Объявляем МАГАЗИН!!! :\n')
shop = Shop()

pr_1 = Product('Картофель', 3.1 , 'Овощи')
pr_2 = Product('Огурцы', 0.6 , 'Овощи')
pr_3 = Product('Помидоры', 0.5 , 'Овощи')
pr_4 = Product('Лук', 1.2 , 'Овощи')
pr_5 = Product('Вермишель', 0.4 , 'Бакалея')
pr_6 = Product('Рис', 0.3 , 'Бакалея')

shop.add(pr_1, pr_2, pr_3, pr_4, pr_5, pr_6)

print('\nЗагружаем продукты и смотрим ассортимент :\n')
shop.get_products()

print('\nЕщё загружаем продукты :\n')
pr_7 = Product('Килька', 0.5 , 'Консервы')
pr_8 = Product('Маринованный огурцы', 0.5 , 'Консервы')
pr_9 = Product('Ветчина заморская', 0.3 , 'Мясопродукты')
pr_10 = Product('Грибы', 1.2 , 'Бакалея')

shop.add(pr_7, pr_8, pr_9, pr_10, pr_6, pr_5, pr_7)

print('\nСмотрим ассортимент :\n')
shop.get_products()


print('\nПовторно загружаем те же продукты:\n')
shop.add(pr_1, pr_2, pr_3, pr_4, pr_5, pr_6)
print('\nСмотрим...:\n')
shop.get_products()
print('А ассортимент всё тот же...')




