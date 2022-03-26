class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(self.name + "can walk")


class Human:
    def __init__(self,name):
        self.name = name
    def talk(self):
        print(self.name + "can talk")


class Dog(Animal):
    def bark(self):
        print(self.name + "can bark")


if __name__ == '__main__':
    animal = Animal('jerry')
    animal.walk()

    jim = Human('jim')
    jim.talk()

    dog = Dog('tom')
    dog.bark()
    dog.walk()
