name = input("What is your name?")
age = 55
n = int(input("What is your ne'er age?"))

def greatnes():
    if n > age:
        print("You,{name} are a great ne'er")
    elif n < age:
        print(f"You,{name} are too young to be a great ne'er")
        return greatnes()