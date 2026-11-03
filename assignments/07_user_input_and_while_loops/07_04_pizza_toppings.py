# Mike Goodman 
# Best toppings for pizza 
# 3/10 

prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"I'll add {topping} to your pizza.")

print("Your pizza order is finished.")