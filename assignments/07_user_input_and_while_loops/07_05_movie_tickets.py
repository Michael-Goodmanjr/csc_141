# Mike Goodman 
# Movie tickets only buy them online tho 
# 5/10 

while True:
    age = input("\nHow old are you? ")
    age = int(age)

    if age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")

    again = input("Is there another person? (yes/no) ")

    if again == 'no':
        break