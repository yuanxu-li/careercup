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

if __name__ == "__main__":
	import doctest
	doctest.testmod()
