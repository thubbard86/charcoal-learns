#Ask for user's name

def first():
    name = input("What's your name? ").strip().lower()
    first, last = name.split(" ")
    second(first)


#Greet the World and then user, intentionally not capitalizing user name.

def second(to="World"):
    print(f"Hello, {to}")

#Ask for user's favorite color. Antagonize user for poor choice. 

def third():
    color = input("What's your favorite color? ").strip().capitalize()
    print(f"{color}??? That's... nice.")


second()
first()
third()