class Duck:
    def talk(self):
        print('duck talking')
    def walk(self):
        print('duck walking')
class Dog(Duck):
    def eat(self):
        print('dog eat')
    def walk(self):
        super().walk()
        print('dog walk')
d=Dog()
d.eat()
d.walk()
d.talk()

