# Mike Goodman 
# Deli 
# 4/10 

sandwich_orders = ['tuna', 'turkey', 'ham', 'chicken']

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made your {current_sandwich} sandwich.")

    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches were made:")

for sandwich in finished_sandwiches:
    print(sandwich)