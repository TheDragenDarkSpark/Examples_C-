"""

Задача 32: 

Определить индексы элементов массива (списка), значения которых 
принадлежат заданному диапазону (т.е. не меньше заданного минимума 
и не больше заданного максимума)

Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
5
15
Вывод: [1, 9, 13, 14, 19]

"""

list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

## Задаём диапазон значение в массиве:  
minVal = int(input("Введите минимальное значение в массиве: "))
maxVal = int(input("Введите максимальное значение в массиве: "))

## Объявляем функцию для вычисления значений:
def array(l, min, max):
    
    listNum = []
    count = 0
   
    for i in range(len(l)):
        
        if min <= l[i] <= max:
            listNum.append(count)
            
        count += 1
        
    print(*listNum)

## Вызываем функцию для вычисления интерисующих нас позиций в массиве:
array(list_1, minVal, maxVal)

