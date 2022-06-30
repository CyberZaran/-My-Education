nums = [5, 4, 3, 7, 8, 1, 32, 55, 34, 'Cats', 4.5, [3, 4, 6]]
nums[2] = 40 # Изменяем значение 2-го элемента.
print(nums[-1][1]) # Берем значение из списка внутри.


numbers = [5, 7, 1, 22, 7, 7, 455, 55, 2]
numbers.append(100) # Добавляем элемент в конец списка.
numbers.insert(3, 400) # Добавляем новый элемент в любом месте списка.
numbers.extend([4, 5, 60]) # Добавляет несколько элементов в конец списка.
numbers.sort() # Сортирует список по возрастанию.
numbers.reverse() # Переворачивает список с конца на начало.
numbers.pop() # Удаляет последний элемент. Так же можно указать индекс.
numbers.remove(22) # Удаляет значения 22 из списка.
#numbers.clear() # Очищает весь список.
#print(numbers.count(7)) # Подсчитывает сколько значений 7 в списке.
print(len(numbers)) # Показывает размер списка.


boms = [1, 4, 7, 8.5, 'Remove', True]
for x in boms:
	x *= 2 # Умножаем каждый элемент на 2.
	print(x)