lines=["hello world!\n","welcome to python\n"]
with open("example.txt","w")as file:
    file.writelines(lines)