import pyfiglet
import random
import sys

def main():
    # Create a Figlet object
    figlet = pyfiglet.Figlet()

    # Handle command-line arguments
    if len(sys.argv) == 1:
        # No arguments, choose a random font
        font = random.choice(figlet.getFonts())

    elif len(sys.argv) == 3 and sys.argv[1] in ("-f", "--font"):
        # Two arguments, expecting a font name
        font = sys.argv[2]
        try:
            figlet.setFont(font=font)  # Validate font
        except pyfiglet.FontNotFound:
            print(f"Error: Font '{font}' not found.")
            sys.exit(1)
    else:
        print("Usage: python figlet.py [-f | --font] <font_name>")
        sys.exit(1)

    # Get user input and render text in the chosen font
    user_input = input("Input: ").strip()
    figlet.setFont(font=font)
    print("Output:\n", figlet.renderText(user_input))

if __name__ == "__main__":
    main()
