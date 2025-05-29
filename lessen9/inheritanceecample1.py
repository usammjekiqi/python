#class superclas:

#class subclas(superclas):#ketu subklasa trashigon pjes pej superklasese


class anumal:
    def eat(self):
        print("this anemal eats")
    def sleep(self):
        print("it sleep")


class bird(anumal):
    def fly(self):
        print("it flyes in the sky")
    def sings(self):
        print('its sings')


bilbil=bird()
bilbil.sings()
bilbil.fly()