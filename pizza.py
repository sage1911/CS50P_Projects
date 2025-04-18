import sys
from tabulate import tabulate
import csv


if len(sys.argv) != 2:
    print("Usage: python lines.py <filename>")
    sys.exit(1)


filename = sys.argv[1]
if not filename.endswith(".csv"):
    print("Error: Invalid file extension. Please use a .csv file")
    sys.exit(1)    

def csv_reader(filename):
    data = []

    try:
        with open(filename, "r", newline="") as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)

    except FileNotFoundError:
        print("Error: File not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading CSV file: {e}")

    return data    

data = csv_reader(filename)


table = tabulate(data, headers="firstrow", tablefmt="fancy_grid")
print(table)