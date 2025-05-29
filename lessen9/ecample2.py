class animal:
    def sound(self):
        print("some generit anemal sound")

class dog(animal):
    def sound(self):
        print("woof!woof")


class cat(animal):
    def sound(self):
        print("meowf!meowf")

kafsh=animal()

kafsh.sound()
rex=dog()
rex.sound()

tom=cat()
tom.sound()




