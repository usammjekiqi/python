while True:
    user_input=input("Enter a positive number: ")
    if user_input.isnumeric():
        number=int(user_input)
        if number>0:
            break
    print("Invalid")
print("Positive: ",number)