class Z:
    def __init__(self, x=549):
        print(f"Z's constructor: {x}")
        self.x = x

    def get_x(self):
        return self.x


class A(Z):
    def __init__(self, x=42):
        print(f"A's constructor: {x}")
        super().__init__(x)

    def get_x_a(self):
        return self.x


class B(Z):
    def __init__(self, x=108):
        print(f"B's constructor: {x}")
        super().__init__(x)

    def get_x_b(self):
        return self.x


class C(A, B):
    def __init__(self):
        A.__init__(self, 100)
        B.__init__(self, 200)
        print("C's constructor")

    def fun(self):
        self.x += 1


o1 = C()
o1.fun()
print(o1.get_x_a())
print(o1.get_x_b())
print(o1.get_x())
