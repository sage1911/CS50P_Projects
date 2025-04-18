grocery = {}


while True:
    try:
        item = input().strip().lower()
        grocery[item] = grocery.get(item, 0) + 1 

    except EOFError:
        break

for item in sorted(grocery.keys()):
    print(grocery[item], item.upper())





    