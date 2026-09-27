# Password strength 
while True:
    password = input("Enter a password: ")
    # Conditions
    has_upper = False
    has_lower = False
    has_number = False
    has_special = False
    # Loop through each character in the password
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_number = True
        else:
            has_special = True
    # Requirements
    if (len(password) >= 8 and has_upper and has_lower 
        and has_number and has_special):
        print("Strong Password!")
        break
    else:
        print("Weak Password\nTry again.\n")
