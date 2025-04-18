def energy(mass):
    c = 300000000
    return mass * (c ** 2)

user_input = int(input("What is m?: "))
print(energy(user_input))