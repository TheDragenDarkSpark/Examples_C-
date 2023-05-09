"""

Задача 30:  

Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с 
клавиатуры. Формула для получения n-го члена прогрессии: 
    an = a1 + (n-1) * d.
Каждое число вводится с новой строки.

"""

## Вводим начальный элемент прогрессии, её шаг и число элементов:
a = int(input("Введите первый элемент арифметической прогрессии: "))
b = int(input("Введите шаг арифметической прогрессии: "))
n = int(input("введите число элементов в прогрессии: "))

print() 

## Объявляем и записываем функцию для вывода прогрессии:
def arProg (elem, step, lastNumb):
    list_1 = [elem]
    for i in range(lastNumb-1):
        elem += step
        list_1.append(elem)
        
    return list_1

## Выводим значения элементов арифм. прогр. на консоль:        
ar = arProg(a, b, n)    
print(*ar)      