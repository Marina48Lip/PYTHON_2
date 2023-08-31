# Создайте класс Матрица. 
# Добавьте методы для: вывода на печать, сравнения, сложения, 
# *умножения матриц

class matrix:
    def __init__(self, matrix) -> None:
        self.matrix = matrix
    
    def print_m(self, matrix: list):
        return self.matrix
    

    def __eq__(self, __value: object) -> bool:
        return self.matrix == __value.matrix
    
    def __add__(self, other): 
        result = [] 
        for i in range(len(self.matrix)): 
            summa = [self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] 
            result.append(summa)      
        return result

    def __mul__(self, other): 
        result = [] 
        for i in range(len(self.matrix)): 
            row = [] 
            for j in range(len(other.matrix[0])): 
                element = sum(self.matrix[i][k] * other.matrix[k][j] for k in range(len(self.matrix[0]))) 
                row.append(element) 
            result.append(row) 
 
        return result


m1 = matrix([[1, 2], [3, 4]])
m2 = matrix([[1, 3], [3, 4]])
print(m1.print_m(m1))
print(m2.print_m(m2))
print(m1 == m2)
print(m1 + m2)
print(m1 * m2)



        