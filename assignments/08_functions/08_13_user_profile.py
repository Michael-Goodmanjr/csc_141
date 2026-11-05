# Mike Goodman 
# user profiles 
# 7/10 

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last

    return user_info

my_profile = build_profile(
    'Mike',
    'Goodman Jr',
    major='Game and Simulation',
    favorite_game='Rivals',
    hobby='gaming'
)

print(my_profile)