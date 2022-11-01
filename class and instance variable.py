#class variables and istance variables


class Dog:
    def __init__(self,color,breed):
        self.color=color
        self.breed=breed

    def print(self):
        print(self.color,self.breed)