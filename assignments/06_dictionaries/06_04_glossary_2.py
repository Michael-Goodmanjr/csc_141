# Mike Goodman 
# Part2 we back at it 
# dif 3/10 

glossary = {
    'list': 'A list is a collection of items in a particular order.',
    'dictionary': 'A dictionary is a collection of key-value pairs.',
    'for loop': 'A for loop is a control flow statement that allows code to be executed repeatedly.',
    'if statement': 'An if statement is a control flow statement that allows code to be executed based on a condition.',
    'function': 'A function is a block of code that performs a specific task.',
    'string': 'A string is a sequence of characters enclosed in quotes.',
    'integer': 'An integer is a whole number without a decimal point.',
    'float': 'A float is a number with a decimal point.',
    'boolean': 'A boolean is a data type that can have one of two values: True or False.',
    'tuple': 'A tuple is a collection of items that is ordered and unchangeable.'}

for word, meaning in glossary.items():
    print(f"{word.title()}: {meaning}")