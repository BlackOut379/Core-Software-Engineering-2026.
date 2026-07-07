def profile():
    name = input("Enter First Name: ").strip().title()
    surname = input("Enter Last Name: ").strip().title()
    location = input("Enter Location: ").strip().title()
    print(f"Name: {name} {surname}")
    print(f"Location: {location}")

def main():
    profile()
    
main()