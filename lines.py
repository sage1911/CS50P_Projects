import sys

if len(sys.argv) != 2:
    print("Usage: python lines.py <filename>")
    sys.exit(1)


filename = sys.argv[1]
if not filename.endswith(".py"):
    print("Error: Invalid file extension. Please use .py")
    sys.exit(1)

try:
    with open(filename, "r") as f:
        lines = f.readlines()

        code_lines = [line for line in lines if line.strip() and not line.lstrip().startswith("#")]

        print(f"Number of lines: {len(lines)}")
except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)
