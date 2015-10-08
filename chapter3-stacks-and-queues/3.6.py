# 3.6 Animal Shelter: An animal shelter, which holds only dogs and cats, operates
# on a strcitly "first in, first out" basis. People must adopt either the
# "oldest" (based on arrival time) of all animals at the shelter, or they
# can select whether they would prefer a dog or a cat (and will receive the
# oldest animal of that type). They cannot select which specific animal they
# would like. Create the data structures to maintain this system and implement
# operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat. You may
# use the built-in LinkedList data structure.

from enum import Enum
from collections import deque

class AnimalType(Enum):
	dog = 1
	cat = 2

class Animal:
	def __init__(self, name, type_):
		self.name = name
		self.type = type_
	def __str__(self):
		return self.name

class AnimalShelter:
	"""
	>>> as_ = AnimalShelter()
	>>> as_.enqueue(Animal("Justin1", AnimalType.dog))
	>>> as_.enqueue(Animal("Justin2", AnimalType.cat))
	>>> as_.enqueue(Animal("Justin3", AnimalType.dog))
	>>> as_.enqueue(Animal("Justin4", AnimalType.dog))
	>>> print(as_.dequeueCat())
	Justin2
	>>> print(as_.dequeueAny())
	Justin1
	>>> print(as_.dequeueCat())
	None
	>>> print(as_.dequeueDog())
	Justin3
	"""
	def __init__(self):
		self.animals = deque()

	def enqueue(self, animal):
		self.animals.appendleft(animal)

	def dequeueAny(self):
		return self.animals.pop()

	def dequeueDog(self):
		temp_shelter = AnimalShelter()
		animal = self.dequeueAny()
		while animal.type != AnimalType.dog and self.animals:
			temp_shelter.enqueue(animal)
			animal = self.dequeueAny()
		if animal.type != AnimalType.dog:
			temp_shelter.enqueue(animal)
			return_dog = None
		else:
			return_dog = animal
		while temp_shelter.animals:
			self.animals.append(temp_shelter.animals.popleft())
		return return_dog

	def dequeueCat(self):
		temp_shelter = AnimalShelter()
		animal = self.dequeueAny()
		while animal.type != AnimalType.cat and self.animals:
			temp_shelter.enqueue(animal)
			animal = self.dequeueAny()
		if animal.type != AnimalType.cat:
			temp_shelter.enqueue(animal)
			return_cat = None
		else:
			return_cat = animal
		while temp_shelter.animals:
			self.animals.append(temp_shelter.animals.popleft())
		return return_cat

class AnimalModified:
	def __init__(self, name):
		self._name = name
	def __str__(self):
		return str(self._name)
	def set_order(self, order):
		self._order = order
	def get_order(self):
		return self._order

class Dog(AnimalModified):
	def __init__(self, name):
		super(Dog, self).__init__(name)

class Cat(AnimalModified):
	def __init__(self, name):
		super(Cat, self).__init__(name)

class AnimalShelterModified:
	"""
	>>> as_ = AnimalShelterModified()
	>>> as_.enqueue(Dog("Justin1"))
	>>> as_.enqueue(Cat("Justin2"))
	>>> as_.enqueue(Dog("Justin3"))
	>>> as_.enqueue(Dog("Justin4"))
	>>> print(as_.dequeueCat())
	Justin2
	>>> print(as_.dequeueAny())
	Justin1
	>>> print(as_.dequeueCat())
	None
	>>> print(as_.dequeueDog())
	Justin3
	"""
	def __init__(self):
		self.dogs = deque()
		self.dog_size = 0
		self.cats = deque()
		self.cat_size = 0
		self.order = 0

	def enqueue(self, animal):
		if type(animal).__name__ == "Dog":
			animal.set_order(self.order)
			self.order += 1
			self.dogs.appendleft(animal)
			self.dog_size += 1
		elif type(animal).__name__ == "Cat":
			animal.set_order(self.order)
			self.order += 1
			self.cats.appendleft(animal)
			self.cat_size += 1

	def dequeueAny(self):
		if self.cat_size == 0:
			return self.dequeueDog()
		elif self.dog_size == 0:
			return self.dequeueCat()
		else:
			dog = self.dequeueDog()
			cat = self.dequeueCat()
			if dog.get_order() < cat.get_order():
				self.cats.append(cat)
				self.dog_size -= 1
				return dog
			else:
				self.dogs.append(dog)
				self.cat_size -= 1
				return cat

	def dequeueCat(self):
		if self.cat_size == 0:
			return None
		else:
			self.cat_size -= 1
			return self.cats.pop()

	def dequeueDog(self):
		if self.dog_size == 0:
			return None
		else:
			self.dog_size -= 1
			return self.dogs.pop()

if __name__ == "__main__":
	import doctest
	doctest.testmod()
