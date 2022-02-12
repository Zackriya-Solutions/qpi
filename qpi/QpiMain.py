class Qpi:
    
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
        self.sum = self.summer(self.a, self.b)
    
    def summer(a, b):
        sum = a + b
        return sum