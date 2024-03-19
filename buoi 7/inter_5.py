class AnimalShelter:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, animal):
        self.s1.append(animal)

    def dequeue_any(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def dequeue_dog(self):
        if not self.s2:
            while self.s1:
                animal = self.s1.pop()
                if animal.type == "dog":
                    return animal
                else:
                    self.s2.append(animal)
        return self.s2.pop()

    def dequeue_cat(self):
        if not self.s2:
            while self.s1:
                animal = self.s1.pop()
                if animal.type == "cat":
                    return animal
                else:
                    self.s2.append(animal)
        return self.s2.pop()

class Animal:
    def __init__(self, type, arrival_time):
        self.type = type
        self.arrival_time = arrival_time

# Ví dụ sử dụng
shelter = AnimalShelter()

dog1 = Animal("dog", 1)
cat1 = Animal("cat", 3)
cat2 = Animal("cat", 4)

shelter.enqueue(dog1)
shelter.enqueue(cat1)
shelter.enqueue(cat2)

print(shelter.dequeue_any().type)
print(shelter.dequeue_dog().type)
print(shelter.dequeue_cat().type)