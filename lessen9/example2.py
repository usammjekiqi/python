from lessen9.ecample2 import kafsh


class dog:
    def __init__(self,name):
        self.name=name

    def sound(self):
        print(f"{self.name} nake the sound: ham")


class cat:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} nake the sound: miau")


class bird:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} nake the sound: ciu")



qeni= dog("reksi")
macja= cat("oreo")
zogu = bird("tik")


for kafsh in (qeni, macja ,zogu):
    kafsh.sound()