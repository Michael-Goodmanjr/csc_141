# Mike
# 3 
#3/10

favorite_numbers = {
    'Mike': [7, 13],
    'John': [12, 20],
    'Sarah': [4, 8],
    'Alex': [10, 25],
    'Chris': [3, 21],
}

for name, numbers in favorite_numbers.items():
    print(f"{name}'s favorite numbers are:")

    for number in numbers:
        print(number)

    print()