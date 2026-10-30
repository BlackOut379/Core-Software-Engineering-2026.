def main():
    while True:
        try:
            first=float(input("Enter First number of operation:"))
            second=float(input("Enter Second Number of operation:"))
            symbol=input("Enter the symbol of operand:").strip()
            if symbol=="/" and second==0:
                raise ZeroDivisionError
            if symbol not in ("+", "-", "*", "/"):
                raise ValueError("Invalid symbol")
        except ValueError as e:
            if str(e) == "Invalid symbol":
                print("Please enter a valid operator (+, -, *, /).")
            else:
                print("Please enter valid numbers.")
        except ZeroDivisionError:
                print("For a division second number cannot be zero.")
        else:
            break
    x=operation(first,second,symbol)
    print("Answer:",x)

def operation(first,second,symbol):
    if symbol=="+":
        return first+second
    elif symbol=="-":
        return first-second
    elif symbol=="*":
        return first*second
    elif symbol=="/":
        return first/second

main()
