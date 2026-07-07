def profile():
    name = input("Enter First Name: ")
    surname = input("Enter Last Name: ")
    location = input("Enter Location: ")
    print(f"Name: {name.strip().title()} {surname.strip().title()}")
    print(f"Location: {location.strip().title()}")

def main():
    profile()
    
main()