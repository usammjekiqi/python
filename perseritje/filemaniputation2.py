import os
if os.path.exists("example.txt"):
    print("file exists!!!")



name="usam"
age=17

with open("output.txt","w") as file:
    file.write("name:"+name+"\n")
    file.write("name:" +str(age)+ "\n")