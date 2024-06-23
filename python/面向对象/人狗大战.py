class Person:
    def __init__(self, name, age, sex,relation):
        self.name = name
        self.age = age
        self.sex = sex
        self.parter = None
        self.relation=relation

class Relationship:
    def __init__(self):
        self.couple=[]

    def make_couple(self,obj_1,obj_2):
        self.couple=[obj_1,obj_2]
        print("%s和%s确定了关系"%(obj_1.name,obj_2.name))

    def get_my_parter(self,obj):
        print("找%s的对象"%obj.name)
        for i in self.couple:
            if i!= obj:
                return i
        else:
            print("没对象啊")

    def break_up(self):
        print("%s 和 %s 分手了"%(self.couple[0].name,self.couple[1].name))
        self.couple.clear()

'''
class Dog:
    def __init__(self, name, age, type):
        self.name = name
        self.age = age
        self.type = type

    def say_hi(self):
        print("hello,my type is %s,my name is %s,i am %d years old"
              % (self.type, self.name, self.age))
'''
relation_obj = Relationship()
p1 = Person("xzc", 23, "M",relation_obj)
p2 = Person("czx", 23, "F",relation_obj)

relation_obj.make_couple(p1,p2)
print(p2.relation.get_my_parter(p2).name)
p1.relation.break_up()
p2.relation.get_my_parter(p2)