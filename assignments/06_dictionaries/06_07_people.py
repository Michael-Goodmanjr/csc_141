# Mike Goodman 
# Program contains a useful list of people 
# SIGH 

person1 = { 'first_name': 'John',
 'last_name': 'Doe',
 'age': 30, 
 'city': 'New York' } 

person2 = { 'first_name': 'Mike',
 'last_name': 'Goodman',
 'age': 18,
 'city': 'Baltimore' } 

person3 = { 'first_name': 'Jane', 
 'last_name': 'Smith',
 'age': 25,
 'city': 'Los Angeles' }

people = [person1, person2, person3]

for person in people:
    print(f"Name:{person['first_name']} {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
    print()
    