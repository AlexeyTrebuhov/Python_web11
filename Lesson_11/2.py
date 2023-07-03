# Создайте класс Архив. который хранит пару свойств. Например. число и строку.
# При создании нового экземпляра класса, старые данные из ранее созданных
# экземпляров сохраняются в пару списков-архивов
# list-архивы тоже являются свойствами экземпляра

# добавьте к задачам 1 и 2 строки документации для классов

# Добавьте методы представления экземпляра для программиста и для пользователя

class Archive:
    '''Сохраняем данные каждого экземпляра класса в списки numbers и values.'''

    numbers = []
    values = []

    def __new__ (cls,number: int, value: str):
        '''переопределяем метод new для сохранения аргументов в списке.'''
        instance = super().__new__(cls)
        cls.numbers.append(number)
        cls.values.append(value)
        return instance

    def __init__(self, number: int, value: str):
        '''Оперделили метод инициализации экземпляров класса.'''
        self.number = number
        self.value = value

    def __repr__(self):
        '''Метод представления экземпляра для программиста'''
        return f'Archive({self.number}, "{self.value}")'

    def __str__(self):
        '''Метод представления экземпляра для пользователя'''
        return f'Номер:{self.number}, Значение: "{self.value}"'

if __name__ == "__main__":
    a_1 = Archive(1, "One")
    a_2 = Archive(2, "Too")
    print(f'{a_1.numbers} {a_1.values}')
    print(f'{a_2.numbers} {a_2.values}')
    a_3 = Archive(3,"Tree")
    print(f'{a_3.numbers} {a_3.values}')
    #help(Archive)
    #help(a_1)
    print(a_1.__repr__())
    print(f'{a_1 = }')
    print(a_1)
