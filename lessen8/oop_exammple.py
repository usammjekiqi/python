class rectangel:
    def __init__(self,lenght,Width):
        self.lenght = lenght
        self.Width =Width

    def calculater_area(self):
        return self.lenght* self.Width

    def calculate_permetur(self):
        return 2 * ( self.lenght + self.Width)


my_recrangle= rectangel(2,4)
area = calculater_area()
preimeter = calculate_permetur()

print(f"area:{area}")
print(f"preimeter:{preimeter}")




