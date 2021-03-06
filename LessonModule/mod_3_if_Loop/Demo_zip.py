"""
Функция zip() в Python создает итератор, который соединяет элементы из двух и более списков.
  Возвращает итератор кортежей, где i-й кортеж содержит i-й элемент из каждой последовательности аргументов или итераций.
   Итератор останавливается, когда самая короткая входная итерация исчерпана.
   С единственным итерируемым аргументом, он возвращает итератор из 1 кортежа.
   Без аргументов возвращает пустой итератор
"""

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)
print(zipped) # iterator object - <zip object at 0x7fa4831153c8>
print(type(zipped))     # <class 'zip'>
print(list(zipped))     # [(1, 'a'), (2, 'b'), (3, 'c')] --- элементы имеют строгий порядок

s1 = {22, 33, 11}   # не хранят свои элементы в каком-либо определенном порядке
s2 = {'b', 'a', 'c'}
print(list(zip(s1, s2)))    # [(33, 'a'), (11, 'b'), (22, 'c')] --- элементы спарены случайным образом
      
zipped = zip() # пустой итератор
print(zipped) # <zip object at 0x7f196294a488>
print(list(zipped)) # [] - рустой список

# Передача аргументов неравной длины

# количество элементов будет равно длине самой короткой итерации
# Остальные элементы в любых более длинных итерациях будут игнорироваться 
print(list(zip(range(5), range(100)))) # [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]

# С помощью функции zip_longest пропущенные значения будут заменены тем,
# что передадите аргументу fillvalue (по умолчанию None).
# Итерации будут продолжаться до тех пор, пока не будет исчерпана самая длинная итерация
from itertools import zip_longest
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
longest = range(5)
zipped = zip_longest(numbers, letters, longest, fillvalue='?')
print(list(zipped))     # [(1, 'a', 0), (2, 'b', 1), (3, 'c', 2), ('?', '?', 3), ('?', '?', 4)]


"""
Распаковка последовательности
"""
pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
numbers, letters = zip(*pairs)
print("Распаковка:", numbers, letters)     # (1, 2, 3, 4) ('a', 'b', 'c', 'd')

"""
Параллельное прохождение списков
Функция zip() позволяет выполнять параллельные итерации по двум и более последовательностям. 
Поскольку zip() генерирует кортежи, вы можете распаковать их в заголовке цикла for: 
"""
letters = ['a', 'b', 'c']
operators = ['*', '/', '+']
numbers = [0, 1, 2]
for l, n, o in zip(letters, numbers, operators):
    print(f'Letter: {l}')
    print(f'Number: {n}')
    print(f'Operator: {o}')

"""
Параллельная обработка словарей

Cловари являются упорядоченными коллекциями, то есть они хранят свои элементы в том же порядке,
в котором они были созданы.
Можно использовать функцию zip() для безопасного и последовательного перебора нескольких словарей:
"""
dict_one = {'name': 'John', 'last_name': 'Doe', 'job': 'Python Consultant'}
dict_two = {'name': 'Jane', 'last_name': 'Doe', 'job': 'Community Manager'}
for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
    print(k1, '->', v1)
    print(k2, '->', v2)


"""
Параллельная сортировка

Требуется: объединить два списка и отсортировать их одновременно.
Решение 1: Применить zip() вместе с .sort() следующим образом:
Сначала объединяются два списка с помощью zip() и затем сортируются.
data1 сортируются по letters, а data2 – по numbers.
"""
letters = ['b', 'a', 'd', 'c']
numbers = [2, 4, 3, 1]
data1 = list(zip(letters, numbers))
print(data1)            # [('b', 2), ('a', 4), ('d', 3), ('c', 1)]
data1.sort()            # Sort by letters
print(data1)            # [('a', 4), ('b', 2), ('c', 1), ('d', 3)]

data2 = list(zip(numbers, letters))
print(data2)            # [(2, 'b'), (4, 'a'), (3, 'd'), (1, 'c')]
data2.sort()            # Sort by numbers
print(data2)            # [(1, 'c'), (2, 'b'), (3, 'd'), (4, 'a')]

"""
Решение 2. Использовать sorted() и zip() вместе:
В этом случае sorted() проходит через итератор, сгенерированный zip (),
и сортирует элементы по letters, и все за один раз.
"""
letters = ['b', 'a', 'd', 'c']
numbers = [2, 4, 3, 1]
data = sorted(zip(letters, numbers)) # Sort by letters
print(data)             # [('a', 4), ('b', 2), ('c', 1), ('d', 3)]

"""
Вычисления в парах

Дано: следующие данные в электронной таблице:
Element/Month	January	February	March
Total Sales	52,000.00	51,000.00	48,000.00
Production Cost	46,800.00	45,900.00	43,200.00
Требуется: посчитать ежемесячную прибыть.
Решение: zip() - быстрый способ сделать эти вычисления:
"""
total_sales = [52000.00, 51000.00, 48000.00]
prod_cost = [46800.00, 45900.00, 43200.00]

for sales, costs in zip(total_sales, prod_cost):    # Функция zip() объединяет правильные пары данных для выполнения расчетов
    profit = sales - costs                          # рассчитывается прибыль за каждый месяц
    print(f'Total profit: {profit}')
"""
Total profit: 5200.0
Total profit: 5100.0
Total profit: 4800.0
"""

"""
Создание словарей

Дано два списка.
Требуется создать словарь из двух разных, но тесно связанных последовательностей.
Решение: использовать dict() и zip()
zip(fields, values) возвращает итератор, который генерирует кортежи из 2 элементов
Если вызвать dict() для этого итератора, то таким образом создастся словарь.
Элементы первого списка становятся ключами словаря, а элементы второго - значениями.
"""
fields = ['name', 'last_name', 'age', 'job']
values = ['John', 'Doe', '45', 'Python Developer']

a_dict = dict(zip(fields, values))
print(a_dict)       # {'name': 'John', 'last_name': 'Doe', 'age': '45', 'job': 'Python Developer'}


"""
Обновление словарей
Можно обновить существующий словарь, комбинируя zip() с dict.update().
Сценарий: Джон меняет работу, и нужно обновить словарь.
Решение:
"""
new_job = ['Python Consultant']
field = ['job']
a_dict.update(zip(field, new_job))
"""
dict.update() обновляет словарь с помощью кортежа значения ключа,
который вы создали с помощью функции zip().
"""
print(a_dict)       # {'name': 'John', 'last_name': 'Doe', 'age': '45', 'job': 'Python Consultant'}







