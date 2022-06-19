class robot:
	# Переменные в классах называются "Поля"
	model = None
	movement = None
	speed = None
	specialization = None

	# Функция внутри класса называется как "Метод"
	def set_data(self, model, movement, speed, specialization):
		self.model = model
		self.movement = movement
		self.speed = speed
		self.specialization = specialization

	def get_data(self):
		print(" ", self.model,"\n", "movement:", self.movement, "\n", "speed:", self.speed, "\n", "specialization:", self.specialization, "\n")

Robot1 = robot()
Robot1.set_data("N100", "По земле", 20, "Уборщик")

Robot2 = robot()
Robot2.set_data("M170", "Полет", 80, "Строитель")

Robot1.get_data()
Robot2.get_data()