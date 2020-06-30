'''
python实战作业二
课后作业：自己写一个面向对象的例子
创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
创建子类【猫】，继承【动物类】，
- 复写父类的__init__方法，继承父类的属性，
- 添加一个新的属性，毛发=短毛，
- 添加一个新的方法， 会捉老鼠，
- 复写父类的‘【会叫】的方法，改成【喵喵叫】
创建子类【狗】，继承【动物类】，
- 复写父类的__init__方法，继承父类的属性，
- 添加一个新的属性，毛发=长毛，
- 添加一个新的方法， 会看家，
- 复写父类的【会叫】的方法，改成【汪汪叫】
创建一个猫猫实例
- 调用捉老鼠的方法
- 打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】。
创建一个狗狗实例
- 调用【会看家】的方法
- 打印【狗狗的姓名，颜色，年龄，性别，毛发】。
使用 yaml 来管理实例的属性
'''
import yaml


class Animal():
    name: str = "puppy"
    color: str = "white"
    age: int = 7
    sex: str = "boy"

    def __init__(self, name, color, age, sex):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex

    def roar(self):
        return "会叫"

    def run(self):
        return "会狂奔"


class Cat(Animal):
    hair: str = "长毛"

    def catch(self):
        return "抓到老鼠了～～"

    def roar(self):
        return "喵喵叫"


class Dog(Animal):
    hair: str = "长毛"

    def keep(self):
        return "会看家～～"

    def roar(self):
        return "汪汪叫"


datas = yaml.safe_load(open("datas.yml"))
cat = datas['cat']
dog = datas['dog']
mew = Cat(cat['name'], cat['color'], cat['age'], cat['sex'])
dog = Dog(dog['name'], dog['color'], dog['age'], dog['sex'])
# mew = Cat("jassica", "灰色", 2, "姑娘")
# dog = Dog("阿奇", "金色", 1, "男孩")
print(f"{mew.name}是一只{mew.color}猫，今年{mew.age}岁，{mew.hair},是个{mew.sex}，" + mew.catch() + mew.roar())
print(f"{dog.name}是一只{dog.color}狗，今年{dog.age}岁，{dog.hair},是个{dog.sex}，" + dog.keep() + dog.roar())
