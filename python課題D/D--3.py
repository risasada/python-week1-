import math


class Square:

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def diagonal(self):
        return round(math.sqrt(self.side ** 2 + self.side ** 2), 2)


square1 = Square(side=1.5)
print(square1.area())  # 2.25
print(square1.diagonal())  # 2.12
