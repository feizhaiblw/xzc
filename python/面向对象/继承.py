class Animal:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def eat(self):
        print("%s is eating"%self.name)

class Person(Animal):
    def __init__(self,name,age,sex,hobby):
        super().__init__(name,age,sex)
        self.hobby=hobby
    def eat(self):
        Animal.eat(self)
        print("%s is eating 2"%self.name)

p=Person("11",11,'M',"a")
p.eat()