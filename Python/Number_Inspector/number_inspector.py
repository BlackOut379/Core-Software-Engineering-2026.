def main():
    n=int(input("Enter a positive Integer: "))
    count(n)
    total(n)
    largest(n)
    rev(n)

def count(n):
    count=0
    while n!=0:
        n=n//10
        count+=1
    print("Digit count:", count)

def total(n):
    total=0
    while n!=0:
        x=n%10
        n=n//10
        total+=x
    print("Digit total:", total)

def largest(n):
    large=0
    while n!=0:
        x=n%10
        n=n//10
        if large<x:
            large=x      
    print("Largest digit:", large)

def rev(n):
    number=0
    while n!=0:
        x=n%10
        number= number*10+x
        n=n//10
    print("Reversed number:", number)


main()
