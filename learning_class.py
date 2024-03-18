class circle():
	def __init__(self, radius):
		self.radius = radius
	def __str__(self):
		return f"circle radius:{self.radius}"
first_circle = circle(15)
second_circle = circle(21)
print(first_circle)
print(second_circle)


class square():
	def __init__(self, width):
		self.width = width
	def __str__(self):
		return f"square width:{self.width}"
first_square = square(15)
second_square = square(21)
print(first_square)
print(second_square)

class Book():
	def __init__(self, pages):
		self.pages = pages
	def __str__(self):
		return f"book pages:{self.pages}"
book_page = Book(100)
print(book_page)


class Dog():
    def __init__(self, eyes, tail, legs):
    	self.eyes = eyes
    	self.tail = tail
    	self.legs = legs

    def __str__(self):
    	return f"eyes:{self.eyes} tail:{self.tail} legs:{self.legs}"

dog1 = Dog(2, 1, 4)
dog2 = Dog(1, 2, 4)
dog3 = Dog(4, 1, 2)

print(dog1)
print(dog2)
print(dog3)


class cat():
	def __init__(self, eyes, tail, legs):
		self.eyes = eyes
		self.tail = tail
		self.legs = legs

	def __str__(self):
		return f"eyes:{self.eyes} tail:{self.tail} legs:{self.legs}"

cat1 = cat(2, 1, 3)
cat2 = cat(1, 3, 2)
cat3 = cat(3, 2, 1)

print(cat1)
print(cat2)
print(cat3)

class fan():
	def __init__(self, blades, legs):
		self.blades = blades
		self.legs = legs
	def __str__(self):
		return f"blades:{self.blades} legs:{self.legs}"

fan1 = fan(4, 3)
fan2 = fan(4, 3)

print(fan1)
print(fan2)

class phone():
	def __init__(self, screen, button):
		self.screen = screen
		self.button = button
	def __str__(self):
		return f"screen:{self.screen} button:{self.button}"

phone1 = phone(1, 19)
phone2 = phone(1, 19)

print(phone1)
print(phone2)