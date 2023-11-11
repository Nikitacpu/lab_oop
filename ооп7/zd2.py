class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    @property
    def c(self):
        return self.a**2 - 1.7*self.b
