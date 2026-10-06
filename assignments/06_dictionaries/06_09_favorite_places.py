# Mike Goodman 
# I travled a lot through out my life my mom loves to travel 
# 4/10

favorite_places = {
    'Mike': ['Italy', 'Germany', 'France'],
    'Jakeem': ['Japan', 'China', 'Thailand'],
    'Deslavo': ['Mexico', 'Canada', 'Brazil'],
}

for name, places in favorite_places.items(): 
    print(f"{name}'s favrite places are:")

    for place in places:
        print(f"-{place}')") 

    print()
    