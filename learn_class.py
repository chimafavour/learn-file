

# class Rectangle():
# 	def __init__(self, width, height):
# 		self.width = width
# 		self.height = height

# 	def __str__(self):
# 		return f"Rectangle Width: {self.width} Height: {self.height}"


# first_rec = Rectangle(4, 5)
# second_rec = Rectangle(7, 15)
# print(first_rec)
# print(second_rec)


class Car():
	def __init__(self, name, color):
		self.name = name
		self.color = color

	def move(self):
		print(f"{self.name} is moving.")

	def __str__(self):
		return f"{self.name} Car with {self.color} Color"


first_car = Car("Toyota", "green")
second_car = Car("Golf", "silver")

print(first_car)
first_car.move()


print(second_car)
