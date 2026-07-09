def main():
    mass = int(input("Enter Mass in kg:"))
    print("Energy in joules:", Energy(mass))
    

def Energy(mass):
     c=300000000
     E = mass*c**2
     return E
    
main()