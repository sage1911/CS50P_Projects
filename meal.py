def main():
    user_input = input("What time is it?: ")
    time_in_hours = convert(user_input)        

    if 7.0 <= time_in_hours <= 8.0:
        print("Breakfast time")
    elif 12.0 <= time_in_hours <= 13.0:
        print("Lunch time")
    elif 18.0 <= time_in_hours <= 19.0:
        print("Dinner time")    

 



def convert(time):
    hours, minutes = time.split(":")    
    return int(hours) + int(minutes) / 60 


if __name__ == "__main__":
    main()    