class ArithmeticProgression:
    def __init__(self, first, x):
        self.first = first
        self.num = first
        self.x = x

    def __iter__(self):
        return self

    def __next__(self):
        res = self.num
        self.num = self.num+self.x
        return res


class GeometricProgression(ArithmeticProgression):
    def __next__(self):
        res = self.num
        self.num = self.num * self.x
        return self.num
progression = ArithmeticProgression(0, 1)

for elem in progression:
    if elem > 10:
        break
    print(elem, end=' ')
