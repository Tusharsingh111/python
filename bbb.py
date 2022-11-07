"""hierarichal inheritance"""
class Parent:
    def func1(self):
        print("Base class function")

class Child1(Parent):
    def func2(self):
        self.func1()
        print("Child class 1 function")

class Child2(Parent):
    def func3(self):
        self.func1()
        print("Child class 2 function")

c1=Child1()
c1.func2()
c2=Child2()
c2.func3()
