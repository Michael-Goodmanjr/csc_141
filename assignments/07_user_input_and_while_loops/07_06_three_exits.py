# Mike Goodman 
# 3 exits 
# 1/10 

topping = ""

while topping != 'quit':
    topping = input("Enter a pizza topping or 'quit': ")

    if topping != 'quit':
        print(f"I'll add {topping} to your pizza.")


# Version 2: Active variable

active = True

while active:
    topping = input("Enter a pizza topping or 'quit': ")

    if topping == 'quit':
        active = False
    else:
        print(f"I'll add {topping} to your pizza.")


# Version 3: Break statement

while True:
    topping = input("Enter a pizza topping or 'quit': ")

    if topping == 'quit':
        break

    print(f"I'll add {topping} to your pizza.")