def main():
    m = float(input("Enter metre value:"))
    print("Centimetre value is", converter(m))


def converter(x):
    return x*100


main()  