name = input("Enter a list of names: ").split()
 
with open("names.txt", "a") as file:

    file.write(f"{name}\n")
