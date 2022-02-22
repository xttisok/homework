"""
1. 简答题
1、写一个面向对象的例子：
 比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
 创建子类【猫】，继承【动物类】
 重写父类的__init__方法，继承父类的属性
 添加一个新的属性，毛发=短毛
 添加一个新的方法， 会捉老鼠，
 重写父类的【会叫】的方法，改成【喵喵叫】
 创建子类【狗】，继承【动物类】
 复写父类的__init__方法，继承父类的属性
 添加一个新的属性，毛发=长毛
 添加一个新的方法， 会看家
 复写父类的【会叫】的方法，改成【汪汪叫】
2、在入口函数中创建类的实例
 创建一个猫猫实例
 调用捉老鼠的方法
 打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】
 创建一个狗狗实例
 调用【会看家】的方法
 打印【狗狗的姓名，颜色，年龄，性别，毛发】

"""

class  Animal:
    name = ""
    colour =""
    age =""
    gener =""


    def  __init__(self,name,colour,age,genger,shout = "mimi",run ="小跑"):
        self.name =name
        print(f"名字是{self.name}")
        self.colour = colour
        print(f"颜色是{self.colour}")
        self.age =age
        print(f"年龄是{self.age}")
        self.genger =genger
        print(f"性别是{self.genger}")
        # self.shout = shout
        # print(f"叫声是{self.shout}")
        # self.run = run
        # print(f"跑步方式是{self.run}")





class Cat(Animal):
    hair ="short hair"


    def set_Catch(self,nothing):
        self.nothing = nothing
        print(f"捕捉到了{self.nothing}")

    def Shout(self):
        print("喵喵叫")


class Dog(Animal):
    hair ="long hair"


    def set_lookhome(self):
        print("会看家")

    def run(self):
        print("汪汪叫")




if __name__ == '__main__':
    # 姓名，颜色，年龄，性别，毛发，捉到了老鼠】
    Amy = Cat("Amy","white",1,"male")
    print(Amy.hair)
    Amy.set_Catch("老鼠")


    # 创建一个狗狗实例
    #  调用【会看家】的方法
    #  打印【狗狗的姓名，颜色，年龄，性别，毛发】
    Boy = Dog("Boy","blue",2,"male")
    print(Boy.hair)
    Boy.set_lookhome()



