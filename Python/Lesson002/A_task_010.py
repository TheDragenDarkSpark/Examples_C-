"""

Задача 10: 
На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
а некоторые – гербом. Определите минимальное число монеток, 
которые нужно перевернуть, чтобы все монетки были повернуты 
вверх одной и той же стороной. Выведите минимальное количество 
монет, которые нужно перевернуть.

"""

import random
## Вводим число монет!
coins = int(input("Введите число монет, которые лежат на столе: "))
countA = 0
countB = 0

## За 0 мы принимаем числом монет, которые лежат решёткой вверх
## За 1 мы принимаем числом монет, которые лежат гербом вверх
for i in range(coins):
    value = (random.randint(0, 1))
      
    if value == 0:
        countA += 1
    
    else:
        countB += 1
        
        
print(f"Числом монет, которые лежат решёткой вверх = {countA}")
print(f"Числом монет, которые лежат гербом вверх = {countB}")
print("")
    
if countA <= countB:
    print(f"Необходимое число монет которое нужно перевернуть = {countA}")
else:
    print(f"Необходимое число монет которое нужно перевернуть = {countB12}")
        
