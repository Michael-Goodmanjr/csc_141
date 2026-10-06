#  Mike Goodman 
# I love dogs and cats I want a german/husky breed as my dream dog and a Bengal Cat 
# dif 5/10 

pet1 = {
    'animal': 'shepsky',
    'owner': 'Mike',
} 

pet2 = { 
    'animal': 'bengal cat',
    'owner': 'Mike',
}

pet3 = { 'animal': 'golden retriever',
        'owner': 'sarah',
}

pets = [pet1, pet2, pet3]

for pet in pets:
    print(f"Animal: {pet['animal']}")
    print(f"Owner: {pet['owner']}")
    print()

    