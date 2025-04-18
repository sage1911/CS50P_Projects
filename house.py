name = input("What's your name?: ")

match name: 
    case "Harry" | "Hermoine" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherinn")
    case _:
        print("Who?")
