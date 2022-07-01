country = {'code': 'ru', 'name': 'Russia', 'population': '150kk'} # Ключи и их значение.
print(country['name'])

country['code'] = 'RU' # Так можно менять значение ключа.

# Второй способ написания словаря.
count = dict(code = 'ru', name = 'Russia', population = '150kk')
print(count['name'])

for key, value in country.items(): # Для того что бы показать ключ и значение нужен модуль items.
	print(key, "-", value)