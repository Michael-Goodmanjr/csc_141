'''
Mike Goodman 
Checking users for what reason though welp we needa complete the work anyway 
dif 8/10 
'''

current_users = ["Mike", "Caleb", "Coby", "Desalvo", "Jakeem", "Justin"] 

new_users = ["Lamar", "Zay", "Kyle", "Nate", "Derrick","Mark"]

current_users_lower = []

for users in current_users:
    current_users_lower.append(user.lower()) 

for new_user in new_users: 
    if new_user.lower() in current_users_lower:
        print(f"{new_user} is already taken. Please eneter a different username")
    else:
        print(f"{new_user} is available.")