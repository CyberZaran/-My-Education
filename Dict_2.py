# Создаем внутри словаря кортеж и еще один словарь. Списки создавать нельзя.
person = {
	'user_1': {
		'first_name': 'Максим',
		'last_name': 'Аверин',
		'age': 21,
		'address': ('г. Сочи','ул. Мольская', 'д. 112'),
		'email': {'email_1': 'MaxAve@mail.ru', 'email_2': 'Avemax@gmail.ru'}
	}
}

print(person['user_1']['address'][0]) # Выводим определенный элемент.


# Программа "Анкета".
n = input('Введите имя: ')
f = input('Введите фамилию: ')
o = input('Введите отчество: ')

data_base = {
	'first_name_2': n,
	'last_name_2': f,
	'otchestvo': o
}

print(data_base['last_name_2'], data_base['first_name_2'], data_base['otchestvo'])