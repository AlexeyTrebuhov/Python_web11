#   Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать
#   создайте класс Матрица. добавьте методы для :
#   - вывода на печать
#   - сравнения матриц
#   - сложения матриц
#   * - умножения матриц  True-Folse


import copy

class Matrix:

    def __init__(self, matrix):
        '''Определили метод инициализации экземпляров класса.'''
        self.matrix = matrix

    def __str__(self):
        '''Заполняем матрицу пустыми строками по всему объему'''
        s = ''
        for i in range(len(self.matrix)):
            s = s + '\t'.join(map(str,self.matrix[i])) + '\n'
        return s

    def __add__(self, other):
        '''Метод сложения матриц поэлементно'''
        if len(self.matrix) != len(other.matrix): # Проверяем условие, чтобы матрицы были одного размера
            return None
        res = copy.deepcopy(self.matrix)   # Создаем итоговую матрицу методом deepcopy ( не копирует ссылки) исходной матрицы
        for i in range(len(self.matrix)):  # Проходим по исходной матрице и other-матрице и суммируем значения в одинаковых полях
            for k in range(len(self.matrix[i])):
                res[i][k] = self.matrix[i][k] + other.matrix[i][k]
        return Matrix(res)

    def __eq__(self, other):
        '''Метод сравнения матриц поэлементно'''
        if len(self.matrix) != len(other.matrix): # Проверяем условие, чтобы матрицы были одного размера
            return None
        res_eq = copy.deepcopy(self.matrix)   # Создаем итоговую матрицу методом deepcopy ( не копирует ссылки) исходной матрицы
        for i in range(len(self.matrix)):  # Проходим по исходной матрице и other-матрице и сравниваем значения в одинаковых полях
            for k in range(len(self.matrix[i])):
                if(self.matrix[i][k] == other.matrix[i][k]):
                    res_eq[i][k] = 'True'
                else:
                    res_eq[i][k] = 'False'
        return Matrix(res_eq)

if __name__ == '__main__':
    l1 = [[1,2,3],[4,5,6],[7,8,9]]
    l2 = [[1,9,8],[1,5,6],[8,8,9]]
    l3 = [[1,2,3],[4,5,6],[7,8,9]]
    m = Matrix(l1)
    s = Matrix(l2)
    v = Matrix(l3)
    print("Исходная матрица")
    print(m)
    print("other - матрица")
    print(s)
    z = m + s
    print("Матрица после сложения",type(z))
    print(z)

    print("Третья матрица")
    print(v)

    print("Самый простой способ сравнения матриц")
    print('Матрицы l1 и l3 равны' if l1==l3 else 'Матрицы l1 иl3 не равны')
    print('Матрицы l1 и l2 равны' if l1==l2 else 'Матрицы l1 иl2 не равны')
    print("l1 и l3 " ,l1==l3)
    print("l1 и l2 " ,l1==l2)

    print("Сравниваем через метод __eq__ L1 и l3 ", l1.__eq__(l3))







