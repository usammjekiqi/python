class Myclass:
    def __init__(self):
        self.__private_variable ="this is private variable"

    def __private_method(self):
        print("this is private method")


myclass = Myclass()
print(myclass.__private_variable)
print(myclass.__private_method)