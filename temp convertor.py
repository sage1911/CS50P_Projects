def main():
    fahrenheit = int(input("Temperature in fahrenheit: "))
    celcius = (fahrenheit - 32) * 5/9 
    

    if celcius > 30:
        print(f"Temperature in celcius: {celcius: .2f} - It's hot")
    elif celcius < 10:
        print(f"Temperature in celcius: {celcius: .2f} - It's cold")    
    else:
        print(f"Temperature in celcius: {celcius: .2f}")    

main()    
