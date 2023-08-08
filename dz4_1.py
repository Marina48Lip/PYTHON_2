# Напишите функцию для транспонирования матрицы 
# Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]

def transponse(matrix,matrix_t):
    for i in range(len(matrix[0])):
        row = []
        for item in matrix:
            row.append(item[i])
        matrix_t.append(row)
    return(matrix_t)         
                          
matrix = [[1, 2, 3], [4, 5, 6]]
matrix_t = []

print(matrix)
print(transponse(matrix,matrix_t))
