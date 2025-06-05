import math

class shape:
    def area(self):
        pass

class circle(shape):
    def __init__(self ,radius):
        self.radius=radius

    def area(self):
        return math.pi * self.radius **2


class rectangle(shape):
    def __init__(self, width, height):
        self.width = width
        self.height=height

    def area(self):
        return self.width * self.width


class triangle(shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height



class pik(shape):
    def __init__(self, a, h):
        self.a = a
        self.h = h

    def area(self):
        return  self.a * self.h


Paralelogrami = pik(3 , 4)
rrethi = circle(2)
drejtekendeshi=rectangle(3,4)
trekendeshi = triangle(6, 4 )
print("siperfqja e rrethit eshte",rrethi.area())
print("siperfqja e drejtekendeshit eshte",drejtekendeshi.area())
print("siperfqja e trekendeshi eshte",trekendeshi.area())
print("siperfqja e Paralelogrami eshte",Paralelogrami.area())







