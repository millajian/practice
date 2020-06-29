# python实战一#作业：创建模块，模块里面创建方法，定义有参数，和无参，有返回值和无返回值 的情况，并说明 无返回值的默认返回值。

class person():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def person_info(name, age, sex):  # 有参数
        myinfo = "I'm " + name + ",today is my birthday，I'm " + str(age) + "th now，" + "a lovely " + sex
        return myinfo  # 有返回

    def eat(self):  # 无参数
        print(f"name : {self.name}, age : {str(self.age)}, sex : {self.sex} I'm eating.")  # 无返回值


personaction = person.person_info('milla', '18', 'girl')  # 实例化，传参数
print(personaction)
littlelemon = person('littlelemon', 7, 'little girl')
print(littlelemon.eat())  # 无返回值，默认返回none
