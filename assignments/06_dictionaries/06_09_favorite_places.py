# Mike Goodman 
# I travled a lot through out my life my mom loves to travel 
# 4/10

favorite_places = {
    'Mike': ['New York', 'Florida'],
    'Jakeem': ['California'],
    'Deslavo': ['Paris', 'London', 'Tokyo'],
}

for name, places in favorite_places.items():
    print(f"{name}'s favorite places are:")

    for place in places:
        print(f"- {place}")

    print()