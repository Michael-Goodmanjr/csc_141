# Mike Goodman 
# Dream Vacation 
# 4/10 

responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    vacation = input("If you could visit anywhere, where would you go? ")

    responses[name] = vacation

    repeat = input("Would another person like to answer? (yes/no) ")

    if repeat == 'no':
        polling_active = False

print("\n--- Dream Vacation Results ---")

for name, vacation in responses.items():
    print(f"{name} would like to visit {vacation}.")