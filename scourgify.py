import sys
import csv

# Check command line argument count and assign input and output file names

if len(sys.argv) != 3:
    print("Usage: python lines.py <filename>")
    sys.exit(1)

inputfile, outputfile = sys.argv[1], sys.argv[2]

# Check file extensions and exit if invalid

if not inputfile.endswith(".csv") or not outputfile.endswith(".csv"):
    print("Error: Invalid file extension. Please use a .csv file")
    sys.exit(1)


def csv_reader(inputfile):
    input_data = []

    try:
        with open(inputfile, "r") as input:
            reader = csv.DictReader(input)
            for row in reader:
                first, last = row["name"].split(", ")
                input_data.append({"first": first, "last": last, "house": row["house"]})

    except FileNotFoundError:
        print("Error: File not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        sys.exit(1)

    return input_data


def csv_writer(outputfile, input_data):
    try:
        with open(outputfile, "w", newline="") as outputfile:
            writer = csv.DictWriter(outputfile, fieldnames=["first", "last", "house"])
            writer.writeheader()
            writer.writerows(input_data)

    except Exception as e:
        print(f"Error writing CSV file: {e}")
        sys.exit(1)


input_data = csv_reader(inputfile)  # Read and process input CSV
csv_writer(outputfile, input_data)
