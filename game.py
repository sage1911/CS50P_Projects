import random

while True:
    try:
        level = int(input("Level?: "))
        if level > 0:
            break

    except ValueError:
        pass

correct_guess = random.randint(1, level)    

while True:
    try:        
    

        guess = int(input("Guess?: "))
        
        if guess > 0:

            if guess == correct_guess:
                print("Correct!")
            elif guess < correct_guess:
                print("Too low!")
            else:
                print("Too high!")
        break

    except ValueError:
        pass
        


