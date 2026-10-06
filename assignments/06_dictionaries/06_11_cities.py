# Mike 
# cities 
# 4/10 

cities = {
    'Baltimore': {
        'country': 'United States',
        'population': 777548,
        'fact': 'Known for its role in the American Civil War.'
    },
    'Tokyo': {
        'country': 'Japan',
        'population': 13929286,
        'fact': 'The most populous city in the world.'
    },
    'Paris': {
        'country': 'France',
        'population': 2148327,
        'fact': 'Famous for the Eiffel Tower and the Louvre Museum.'
    }
} 


for city, info in cities.items():
    print(f"{city} is located in {info['country']}.")
    print(f"It has a population of {info['population']}.")
    print(f"Fun fact: {info['fact']}\n")
    print() 