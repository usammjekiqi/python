#Error Handlling Try, Except, Finnaly
#Try - Main code to function that we need
#Except - what happenes if an error happens in the try part
#Finally - Part of code that is always run
from lessen7.typecasting import rezultati

#This is dedicated for errors that programmers do not predict

#First Example
# try:
#     print("Pjesto 2 numra")
#     nr1=int(input("Shkruani num"))
#     nr2 = int(input("Shkruani num"))
#     resultati=nr1/nr2
#     print("Resultati: ", resultati)
# except ZeroDivisionError:
#     print("No / with 0")

#Second Example
fruits={
    "Apples":5,
    "Bannanas":6,
    "Oranges":7
}
try:
     print(fruits["Bannanas"])
except KeyError:
    print("The key does not exist in the dictionary")

text="This is not a number"
#Third Example
try:
    text_to_int=int(text)
except Exception as e:
    print("An error occorred while parsing the data:", e)


#4 shembull

try:
    rezultati=10/2
except ZeroDivisionError:
    print("devision by zerro error")
else:
    print("devision successful, result",rezultati)



#shembilli 5
try:
    rezultati=10/0
except ZeroDivisionError:
    print("devision by zerro error")
finally:
    print("this part of code always runs")

