# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.

def quarter_of(month):
    pass
    if month in [1, 2, 3]:
        return '1'
    elif month in [4, 5, 6]:
        return '2'
    elif month in [7, 8, 9]:
        return '3'
    elif month in [10, 11, 12]:
        return '4'

month = int(input("Введите номер месяца: "))
print("месяц", month, "является частью", quarter_of(month), "квартала")