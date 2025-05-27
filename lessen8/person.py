class person:
    def  __init__(self,name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"hello, im {self.name}, and im {self.age} years old")



pesoni1 = person("usam",19)
pesoni2 = person("trimi",12)

pesoni1.greet()
pesoni2.greet()


