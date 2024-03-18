class Car():
	def __init__(self, name, color, seat):
		self.name = name
		self.color = color
		self.seat = seat
		self.is_moving = False
		self.is_reversing = True
		self.has_stopped = False
		self.is_turning_right = True
		self.is_turning_left = True

	def move(self):
		if not self.is_moving:
			self.is_moving = True
			print(f"{self.name} is moving.")
		else:
			print("The car is already moving")

	def reverse (self):
		if not self. is_reversing:
			self.is_reversing = False
			print(f"{self.name} is reversing.")

	def stop(self):
		if not self.has_stopped:
			self.has_stopped = True
		print(f"{self.name} has stopped.")

	def horn(self):
		print(f"{self. name} has a horn.")

	def turn_right(self):
		if not self.is_turning_right:
			self.is_turning_right = True
			print(f"{self.name} an indicator that a car is turning right.")

	def turn_left(self):
		if not self.is_turning_left:
			self.is_turning_left = False
		print(f"{self.name} an indicator that a car is turning left.")

	def __str__(self):
		return f"{self.name} car with blue color"


first_car = Car("Matrix ", "Blue", 4)
print(first_car)
first_car.move()
first_car.reverse()
first_car.stop()
first_car.horn()
first_car.turn_right()
first_car.turn_left()