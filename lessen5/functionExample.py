total=0
for number in range(1,11):
    if number%2==0:
        total+=number
print("the sum of number fo 1 ti 10 is",total)

def greet():
    print("hello world!")

greet()

def greet_persone(name):
    print("hello",name)

greet_persone("usam")

def shuma(x,y): #thie type of function return smth in this case a numner
    z=x+y
    return z
rezultati=shuma(3,5)
print("3+5",rezultati)

#local variabel _variabel lokale

def greet(name):
    message=f"hello,{name}!"
    print(message)
greet("usam")


#print(message) -this optputs an error becuse the message variable is defined only for the function


#argunente dhe definimi i tyre
def greet_persone(name, greetting="hello"):
    messag=f"{greetting}, {name}"
    return messag
defalt_greeting=greet_persone("usam")
print(defalt_greeting)
custum_greeting=greet_persone("alam","goodmorning")
print(custum_greeting)




pershendetje="hi!"
def greet_people(name):
    global pershendetje
    return f"{pershendetje}, {name}"
variabel=greet_people("alems")
print(variabel)