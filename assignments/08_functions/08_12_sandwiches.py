# Mike Goodman 
# More Sandwiches???
# 5/10 

def make_sandwich(*items):
    print("\nYour sandwich will include:")

    for item in items:
        print(f"- {item}")

make_sandwich('turkey', 'cheese')

make_sandwich('ham', 'lettuce', 'tomato')

make_sandwich('chicken', 'bacon', 'cheese', 'mustard')