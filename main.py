from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__ (self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        products_file = open (self.__file_name, 'r')
        products = products_file.read()
        products_file.close()
        return products


    def add (self, *products):
        existing_products = self.get_products()
        existing_names = set()
        for line in existing_products.splitlines():
            parts = line.split (', ')
            existing_names.add (parts [0])

        products_file = open (self.__file_name, 'a')

        for product in products:
            if product.name in existing_names:
                print (f'Продукт {product.name} уже есть в магазине')
            else:
                products_file.write (str (product) + '\n')
                existing_names.add (product.name)
        products_file.close()



s1 = Shop ()
p1 = Product ('Tomato', 50.5, 'Vegetables')
p2 = Product ('Potato', 25.6, 'Vegatables')
p3 = Product ('Spaghetti', 3.4, 'Groceries')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())

