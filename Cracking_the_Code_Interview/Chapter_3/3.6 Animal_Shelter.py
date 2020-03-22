# An animal shelter,which holds only dogs and cats,operates on a strictly "first in, first out" basis.People must adopt either the "oldest(based on arrival time)" of all animals at the shelter, or they can select whether they would prefer a dog or a cat(and will receive the oldest animal of that type).They cannot select which specific animal they would like.Create the data structures to maintain this system and implement operations such as enqueue,dequeueAny,dequeueDog,and dequeueCat.You may use the build-in LinkedList data structure. 

class AnimalShelter():
    def __init__(self):
        self.cats,self.dogs = [],[]
    
    def enqueue(self,animal):
        if animal.__class__ == Cat :
            self.cats.append(animal)
        else:
            self.dogs.append(animal)
    
    def dequeueAny(self):
        if len(self.cats):
            return self.dequeueCat()
        else:
            return self.dequeueDog()
    
    def dequeueCat(self):
        if len(self.cats) == 0:
            return None
        cat = self.cats[0]
        self.cats = self.cats[1:]
        return cat

    def dequeueDog(self):
        if len(self.dogs) == 0:
            return None
        dog = self.dogs[0]
        self.dogs = self.dogs[1:]
        return dog


class Animal():
    def __init__(self,name):
        self.name = name
    
    def __str__(self):
        return self.name

class Cat(Animal):pass
class Dog(Animal):pass
        
# if __name__ == '__main__':
#     shelter = AnimalShelter()
#     shelter.enqueue(Cat("Hanlen"))
#     shelter.enqueue(Cat("Pluto"))
#     shelter.enqueue(Dog("Sam"))
#     shelter.enqueue(Dog("Tony"))
#     print(shelter.dequeueAny())
#     print(shelter.dequeueAny())

import unittest

class Test(unittest.TestCase):
  def test_animal_shelter(self):
    shelter = AnimalShelter()
    shelter.enqueue(Cat("Hanzack"))
    shelter.enqueue(Dog("Pluto"))
    shelter.enqueue(Cat("Garfield"))
    shelter.enqueue(Cat("Tony"))
    shelter.enqueue(Dog("Clifford"))
    shelter.enqueue(Dog("Blue"))
    self.assertEqual(str(shelter.dequeueAny()), "Hanzack")
    self.assertEqual(str(shelter.dequeueAny()), "Garfield")
    self.assertEqual(str(shelter.dequeueDog()), "Pluto")
    self.assertEqual(str(shelter.dequeueDog()), "Clifford")
    self.assertEqual(str(shelter.dequeueCat()), "Tony")
    self.assertEqual(str(shelter.dequeueCat()), "None")
    self.assertEqual(str(shelter.dequeueAny()), "Blue")
    self.assertEqual(str(shelter.dequeueAny()), "None")

if __name__ == "__main__":
  unittest.main()