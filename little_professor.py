import random


def main():
    level = get_level()  # Get level from user
    score = 0  # Initialize score

    for i in range(10):  # Loop for 10 problems
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y

        for attempts in range(3):  # Allow up to 3 attempts
            user_input = input(f"{x} + {y} = ")
            if user_input.isdigit() and int(user_input) == answer:
                score += 1  # Increase score if correct
                break  # Exit attempt loop if correct
            print("EEE")  # Show error if wrong

        if (
            not user_input.isdigit() or int(user_input) != answer
        ):  # After 3 wrong attempts
            print(f"The correct answer is: {answer}")

    print(f"Score: {score}/10")  # Show final score


def get_level():
    while True:
        try:
            n = int(input("Choose a level (1, 2, or 3): "))
            if n in [1, 2, 3]:
                return n
        except ValueError:
            pass  # Ignore invalid input and ask again


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Level must be 1, 2, or 3")


if __name__ == "__main__":
    main()
