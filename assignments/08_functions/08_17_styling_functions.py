# Mike Goodman 
# Styling Functions 
# 10/10 

def display_message():
    """Display what I am learning in this chapter."""
    print("I am learning about functions in Python.")


display_message()

def favorite_book(title):
    """Display the title of a favorite book."""
    print(f"One of my favorite books is {title}.")


favorite_book("The God Of High School")

def city_country(city, country):
    """Return a city and country in a formatted string."""
    return f"{city.title()}, {country.title()}"


print(city_country('santiago', 'chile'))
print(city_country('tokyo', 'japan'))
print(city_country('paris', 'france'))