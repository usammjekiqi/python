#ecample of procedure  programming in py

def calculater_area(length, width):
    return length*width
def calculate_permetur(length, width):
    return 2*(length+width)

length=5
width=3

area = calculater_area(length, width)
preimeter = calculate_permetur(length,width)

print(f"area:{area}")
print(f"preimeter:{preimeter}")