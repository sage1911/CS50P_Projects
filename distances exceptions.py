distances = {
    "Voyager 1": "163",
    "Voyager 2": "136",
    "Pioneer 10": "80 AU",
    "New Horizons": "58",
    "Pioneer 11": "44 AU"
}

def main():
    spacecraft = input("Enter a Spacecraft: ")
    try:
        au = float(distances[spacecraft])
    except KeyError:
        print(f"'{spacecraft}' not found")   
        return    
    except ValueError: 
        print(f"Cant convert {distances[spacecraft]} to AU")   
        return
    
    m = convert(au)
    print(f"{m} m away")

def convert(au):
    au * 149597870700

main()
