# Кортеж занимают меньше памяти и их нельзя изменять.
data = (4, 5, 6, 4, 22, 23.2, True, 'Holy') # Можно писать без круглых скобок, просто через запятую.
print(data[1:5]) # Срез от 1 до 5.

# Это все что можно делать с Кортежем.
# print(data.count(6))
# print(len(data))
# print(data)
# (5,) - кортеж из одного элемента.


tuple_test = (4, 5, 6, 4, 22, 23.2, True, 'Holy')
for x in tuple_test:
	print(x)



# Преобразование списка и строки в кортеж.
nums = [2.3, 5, 4, 77, 12]
new_data = tuple(nums) # Преобразование.
word = tuple('Hello Python')
print(new_data)
print(word)