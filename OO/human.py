import abc


# 使用abc实现抽象类，work是人类都需要干的事情，具体的角色，work不一样，留在具体角色函数里实现
class Human(metaclass=abc.ABCMeta):
    sex = ""
    name = ""

    def __init__(self, sex, name):
        self.sex = sex
        self.name = name

    @abc.abstractmethod
    def work(self):
        pass
