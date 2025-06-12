class Digitalschool:
    def __init__(self, name ,city,state,courses):
        self.__name=name
        self.__city = city
        self.__state = state
        self.__courses = courses

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        self.__city = city

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state):
        self.__state = state

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def state(self, courses):
        self.__courses = courses

    def show_school_info(self):
        return {
            "name":self.__name,
            "city":self.__city,
            "state":self.__state,
            "courses":self.__courses
        }

    def organize_hackathon(self):
        print("organizing a generic hackathon.")



#define a ssunclass called da prishtina where it has a private atribute called student number and tweo methodes organiae_hekathon and scf
class ds_prishtina(Digitalschool):
    def __init__(self, name ,city,state,courses , student_number):
        super().__init__(  name ,city,state,courses)
        self.__student_number=student_number
    def SCF(self):
        print("first edicion")
    def organize_hackathon(self):
        print("we are doing a data analysis hackathon")


class ds_ferizaji(Digitalschool):
    def __init__(self, name ,city,state,courses , student_number):
        super().__init__(  name ,city,state,courses)
        self.__student_number=student_number
    def intership(self):
        print("first intership")
    def organize_hackathon(self):
        print("we are doing a data analysis hackathon")



prishtina_obj=ds_prishtina("ds_prishtina ", "prishtina ","kosova",["php","py","java"] ,3000)
prishtina_obj.organize_hackathon()
print(prishtina_obj.show_school_info())




ferizaji_obj=ds_ferizaji("ds_ferizaji ", "ferizaji ","kosova",["php","code1","java"] ,3000)
ferizaji_obj.intership()
print(ferizaji_obj.show_school_info())











