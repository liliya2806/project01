# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

def minimum(arr):
    pass

def maximum(arr):
    pass

list1 = [4,6,2,1,9,63,-134,566]
def get_minimum_maximum(lst):
    minimum = lst[0]
    maximum = lst[0]
    
    for v in lst:
        if v > minimum:
            minimum = v
        if v < maximum:
            maximum = v
    return (minimum, maximum)

result = get_minimum_maximum(list1)
print(f"Максимальное значение: {result[0]}", f"Минимальное значение {result[1]}")



    