class A:
    def __init__(self):
        print("A base class constructor called")

class B:
    def __init__(self):
        print("B base class constructor called")

class C (A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print("C derived class constructor called")

print("Start of program")
c=C()
print("End of program")
