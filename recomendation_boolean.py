def main():
    difficulty = input("Difficult or Casual?")
    if not ( difficulty == "Difficult" or difficulty == "Casual"):
        print("Enter a valid difficulty")
        return
    players = input("Multi-player or Single-player?")    
    if not ( players == "Multi-player" or players == "Single-player"):   
        print("Enter a valid number of players")
        return    

    if difficulty == "Difficult" and players == "Multi-player":
        recommend("Poker")
    elif difficulty == "Casual" and players == "Single-player":
        recommend("Klondike")    
    elif difficulty == "Casual" and players == "Multi-player":
        recommend("Hearts")
    else:
        recommend("Clocks")    



def recommend(game):
    print("You might like", game)
