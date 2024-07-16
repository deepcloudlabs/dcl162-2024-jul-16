class z:
    def __init__(self, x=549):
        self.x = x

class a(z):
    def __init__(self, x=42):
        super().__init__(x)


class b(z):
    def __init__(self, x=108):
        super().__init__(x)

class c(a,b):
    def __init__(self):
        print("__init__ called")

    def fun(self):
        self.x += 1

o1 = c()
o1.fun()