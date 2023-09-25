# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, вычисляющую 
# элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой ровно 
# два аргумента, как, например, у операции умножения.

def print_operation_table(operation, num_rows=6, num_columns=6):
    """ Распечатать таблицу значений операций 
    operation операция, применяемая к номеру строки и столбца 
    num_rows число строк, 
    num_columns число столбцов"""

    for i in range(1, num_rows + 1):
        d = []
        for j in range(1, num_columns + 1):
            result = operation(i, j)
            d.append(result)
        print(*d)

print_operation_table(lambda x, y: x * y)
