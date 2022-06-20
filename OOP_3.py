class robot:
	# Переменные в классах называются "Поля"
	model = None
	movement = None
	speed = None
	specialization = None

	# Создание конструктора.
	def __init__(self, model, movement, speed, specialization):
		self.set_data(model, movement, speed, specialization)
		self.get_data()


	# Функция внутри класса называется как "Метод"
	def set_data(self, model = None, movement = None, speed = None, specialization = None): # Переопределение методов.
		self.model = model
		self.movement = movement
		self.speed = speed
		self.specialization = specialization

	def get_data(self):
		print(" ", self.model,"\n", "movement:", self.movement, "\n", "speed:", self.speed, "\n", "specialization:", self.specialization, "\n")

Robot1 = robot("N100", "По земле", 20, "Уборщик")
Robot1.set_data("N100", "По земле")

Robot2 = robot("M170", "Полет", 80, "Строитель")