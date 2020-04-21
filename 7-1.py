"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""
class Matrix:
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2
    def __add__(self):
        matrix0 = [[0,0,0],
                   [0,0,0],
                   [0,0,0]]
        for i in range(len(self.matrix1)):
            for j in range(len(self.matrix2[i])):
                matrix0[i][j] = self.matrix1[i][j] + self.matrix2[i][j]
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix0]))
    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix0]))

matrix_add = Matrix([[-1, 0, 1],[-2, 2, 3],[4, 5, -5]],
                [[7, 8, 3],[-1, -7, -3],[89, 55, 79]])
print(matrix_add.__add__())
