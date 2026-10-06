# Mike Goodman
# Program contains a poll 
# sigh im tired of this 

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

people_to_poll = ['jen', 'sarah', 'edward', 'phil', 'mike', 'jakeem']

for person in people_to_poll:
    if person in favorite_languages.keys():
        print(f"Thank you for taking the poll, {person.title()}!")
    else:
        print(f"{person.title()}, please take our poll!")