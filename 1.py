import numpy as np 

grades = [59, 98, 63, 92, 88, 70, 51]
grades_array = np.array(grades)

print("Одновимірний масив:", grades_array)



prices = [
    [120.0, 220.0, 293.0, 510.0],  # Ціни в Сільпо
    [130.0, 240.0, 295.0, 540.0],  # Ціни в Ашані
    [100.8, 211.0, 254.0, 478.0],  # Ціни в АТБ
]
prices_matrix = np.array(prices)

print("\nМатриця NumPy (ціни):")
print(prices_matrix)



print("Тип даних у масиві 1:", grades_array.dtype)
print("Тип даних у матриці 2:", prices_matrix.dtype)



print("Форма матриці 1:", prices_matrix.shape)
print("Форма масиву 2:", grades_array.shape)




start_profit = 0  
end_profit = 1000.50  
days = 7

profit_array = np.linspace(start_profit, end_profit, days)

print("Динаміка прибутку за тиждень (грн):")
print(profit_array)






array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

horizontal_stack = np.hstack((array1, array2))
vertical_stack = np.vstack((array1, array2))

print("Масив 1:", array1)
print("Масив 2:", array2)


print(horizontal_stack)
print(vertical_stack)













def transpose_with_reshape(array):
    if len(array.shape) != 2:
        raise ValueError("Масив має бути двовимірним.")
    rows, cols = array.shape
    return array.reshape(cols, rows).T
array3 = np.array([[1, 2, 3], [4, 5, 6]])
transposed_array = transpose_with_reshape(array3)

print("Оригінальний масив:")
print(array3)

print("\nТранспонований масив:")
print(transposed_array)









array4 = np.array([[1, 2, 3], [4, 5, 6]])
array5 = np.array([[6, 5, 4], [3, 2, 1]])
elementwise_addition = array4 + array5
elementwise_subtraction = array4 - array5
scalar_multiplication = array4 * 2
elementwise_multiplication = array4 * array5
matrix_multiplication = np.dot(array4, array5.T)
print("Масив 4:")
print(array4)

print("\nМасив 5:")
print(array5)

print("\n1) По-елементне додавання:")
print(elementwise_addition)

print("\n2) По-елементне віднімання:")
print(elementwise_subtraction)

print("\n3) Множення масиву на число (2):")
print(scalar_multiplication)

print("\n4) По-елементне множення:")
print(elementwise_multiplication)

print("\n5) Матричне множення:")
print(matrix_multiplication)







matrix = np.random.randint(1, 101, size=(5, 5))
min_value = np.min(matrix)
max_value = np.max(matrix)
sum_values = np.sum(matrix)
min_each_row = np.min(matrix, axis=1)
max_each_column = np.max(matrix, axis=0)

print("Матриця:\n", matrix)
print("Мінімальне число:", min_value)
print("Максимальне число:", max_value)
print("Сума чисел:", sum_values)
print("Мінімальні числа для кожного рядка:", min_each_row)
print("Максимальні числа для кожного стовпчика:", max_each_column)















matrix_with_duplicates = np.array([[1, 2, 3, 4, 1],
                                   [5, 6, 7, 8, 1],
                                   [9, 2, 3, 4, 5],
                                   [6, 7, 8, 9, 1],
                                   [2, 3, 4, 5, 6]])
unique_values, counts = np.unique(matrix_with_duplicates, return_counts=True)
print("Матриця2:\n", matrix_with_duplicates)
print("Унікальні       значення:", unique_values)
print("Частоти кожного значення:", counts)