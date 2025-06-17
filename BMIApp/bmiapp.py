from abc import ABC , abstractmethod


class person(ABC):

    def __init__(self , name , age ,weight , height):
        self.name=name
        self.age=age
        self.weight=weight
        self.height=height

    @abstractmethod
    def area(self):
        pass

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        self.name = name

    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, age):
        self.age = age

    @property
    def weight(self):
        return self.weight

    @weight.setter
    def weight(self, weight):
        self.weight = weight

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, height):
        self.height = height

class adult(person):
    def __init__(self, name , age ,weight , height , ):
        super().__init__(self, name , age ,weight ,height)


    def calculato_bmi(self,):
       return self.weight/self.height
    def get_bmi_category(self):
        a=self.calculato_bmi()
        if(a<18):
            print("underweight")
        elif(18<a>24):
            print("normal")
        else:
            print("owerweight")

    def print_info(self):
        return {
            "name":self.name,
            "age": self.age,
            "height": self.height,
            "weight": self.weight

        }


class child(person):
    def __init__(self, name, age, weight, height, ):
        super().__init__(self, name, age, weight, height)


    def calculato_bmi(self):
       return (self.weight / self.height)*1.3

    def get_bmi_category(self):
        bmi = self.calculato_bmi()
        if (bmi < 14):
            print("underweight")
        elif (14 < bmi > 18):
            print("normal")
        else:
            print("owerweight")

    def print_info(self):
        return {
            "name": self.name,
            "age": self.age,
            "height": self.height,
            "weight": self.weight

        }
















