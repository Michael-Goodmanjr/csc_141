# Mike Goodman 
# user profiles 
# 7/10 

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last

    return user_info

my_profile = build_profile(
    'Alex',
    'Morgan',
    major='Game and Simulation',
    favorite_game='Minecraft',
    hobby='coding'
)

print(my_profile)