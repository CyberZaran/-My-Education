def test_func(word): # Если в скобочках записать параметр (переменная), то его можно будет использовать только внутри функции.
	print(word, end="")
	print('!')

test_func("Кошка") # Пишем слово которое будет отображаться вместо "word"


def summa(a, b):
	res = a + b
	print("Result:", res)

summa(6, 8)
summa("H", "i")

# Функция для поиска минимального числа.
def minimal(l):
	min_number = l[0]
	for el in l:
		if el < min_number:
			min_number = el
	print(min_number)


nums1 = [5, 3, 7, 8]
minimal(nums1)

nums2 = [4.5, 3.1, 2.1, 5.6, 7.6, 3.2]
minimal(nums2)

# lambda функция.
func = lambda x, y: x * y
res = func (5, 2)
print(res)