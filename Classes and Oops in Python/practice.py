class Myclass:
    def __init__(self):
        self.var1=10
        self.var2=20
    def func(self):
        return self.a+self.b
        pass
obj=Myclass()
print(obj.__dict__)