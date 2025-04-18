def main():
    while True:
        fraction = input("Enter a fraction in X/Y format: ")
        try:
            percentage = convert(fraction)
            print(gauge(percentage))
            break  # Exit loop after valid input
        except (ValueError, ZeroDivisionError) as e:
            print("Invalid fraction.")


def convert(fraction):
    """
    Converts a fraction string "X/Y" into a percentage (rounded to nearest int).
    Raises:
        - ValueError if X or Y is not an integer, or if X > Y.
        - ZeroDivisionError if Y is 0.
    """
    try:
        x, y = fraction.split("/")
        x, y = int(x), int(y)

        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        if x > y:
            raise ValueError("Numerator must be less than or equal to denominator.")

        return round((x / y) * 100)
    except ValueError:
        raise ValueError("Invalid input: X and Y must be integers.")


def gauge(percentage):
    """
    Converts a percentage integer to a fuel gauge reading.
    """
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
