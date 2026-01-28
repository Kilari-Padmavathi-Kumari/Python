class Duck:
    def talk(self):
        print('duck talking')
    def walk(self):
        print('duck walking')
class Dog:
    def talk(self):
        print('dog eat')
    def walk(self):
        print('dog walk')


def person(pet):
    pet.talk()
    pet.walk()


dog=Dog()
person(dog)
duck=Duck()
person(duck)