# Практическое занятие 4. Применение операторов ветвления и циклов

# Задача 01: Создайте программу и добавьте следующий код, реализующий ядро игры
# (обратите внимание на использование модулей random и time):

from random import randint
import time

# Ввод имен играющих
igrok1 = input('Введите имя 1-го играющего: ')
igrok2 = input('Введите имя 2-го играющего: ')

# Моделирование бросания кубика первым играющим
print('Кубик бросает', igrok1)
time.sleep(2)
n1 = randint(1, 6)
print('Выпало:', n1)

# Моделирование бросания кубика вторым играющим
print('Кубик бросает', igrok2)
time.sleep(2)
n2 = randint(1, 6)
print('Выпало:', n2)

# Задача 02: Реализуйте определение победителя игры. Для этого используйте оператор
# if elif else для реализации выбора из нескольких альтернатив.

#Определение результата (3 возможных варианта)
if n1 > n2:
    print('Выиграл', igrok1)
elif n1 < n2:
    print('Выиграл', igrok2)
else:
    print('Ничья')


