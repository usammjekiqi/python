#decorators getters and setters
class student:
    def __init__(self, name , age):#konstruktori i klases e cila eshte pjes qe ruhen e oara  ketu deklarohen te gjitha atributrt e klases
        self.__name=name
        self.__age=age
    # deklarimi i metodes get
    @property
    def name(self):
        return self.__name

    #deklarimi i metides set
    @name.setter
    def name(self,name):
        self.__name=name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age=age


student1=student("alice", 17)
print("Name:" ,student1.name)


student1.name="bob"
student1.age=18
print("Name:" ,student1.name)