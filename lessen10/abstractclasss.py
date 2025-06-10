from abc import ABC , abstractmethod

class className(ABC): #this is the final defition of abstract class abc is importen
    pass

class shape(ABC):#klas abstrakte
    #metod abstrakte
    @abstractmethod
    def area(self):
        pass

class circle(shape):
    def __init__(self, radius ):
        self.radius=radius

    def area(self):
        return 3.14*self.radius*self.radius


class square(shape):
    def __init__(self,a):
        self.a= a

    def area(self):
        return self.a*self.a


#objektet per keto dy klasa
circle_1=circle(7)
square_1=square(18)
print(circle_1.area())
print(square_1.area())

#klasat abstake mund te kene edhe metoda te thjeshata dhe sbstrake
#interfejsat jane klasa abstrake qe kane vetem metoda anstrake


