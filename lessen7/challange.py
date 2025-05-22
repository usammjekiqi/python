
def calculate(nr1, nr2, operatori):
    if operatori=="+":
        return nr1+nr2
    elif operatori=="-":
        return nr1-nr2
    elif operatori=="*":
        return nr1/nr2
    elif operatori=="/":
        return nr1/nr2
    else:
        raise ValueError("Invalid operator")


try:
    num1=float(input("Enter num1"))
    num2=float(input("Enter num2"))
    operatori=input("Enter an Operation + - * /")
    rezultati=calculate(num1,num2,operatori)
    print(f"The result of {num1} {operatori} {num2} = {rezultati}")

except ValueError as e:
    print(f"Invalid Input {e}")

except ZeroDivisionError as e:
    print(f"Cant Divide BY 0 {e}")

except Exception as e:
    print(f"Error: {e}")

finally:
    print("End of the program")