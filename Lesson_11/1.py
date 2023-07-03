# Создайте класс Моя строка, где будут все возможности str
# дополнительно хранятся имя автора строки и время создания ( time.time)

# добавьте к задачам 1 и 2 строки документации для классов

import time

class MyString(str):
    '''Расширяемый класс str. '''

    def __new__(cls,value:str,name: str):
        '''Расширяем метод new параметрами value и name'''
        instance = super().__new__(cls,value)
        instance.name = name
        instance.created_at = time.time()
        return instance

if __name__ == "__main__":
    mystr = MyString("test_test","dop.parametr")
    print(mystr.created_at)
    print(mystr.name)
    print(mystr)
    print(mystr.upper())
    help(MyString)