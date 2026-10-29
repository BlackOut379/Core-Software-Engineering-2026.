def main():
    n=int(input("Enter Value Of n:"))
    sequence(n)
    total(n)
    parity(n)

def sequence(n):
    print("Sequence: ", end="")
    for i in range(1,n+1):
        print(i, end=" ")
    print()  

def total(n):
    sum=0
    for i in range(n+1):
        sum+=i
    print("Sum:", sum)

def parity(n):
    even=0
    odd=0
    for i in range(1,n+1):
        if i%2==0:
            even+=1
        else:
            odd+=1
    print("Even count:", even)
    print("Odd count:", odd)

main()
