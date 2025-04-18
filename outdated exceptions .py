months = [ 
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    try:
        date = input("Enter a date in MM/DD/YYYY: ").strip()

        if "/" in date:
            month, day, year = date.split("/")

            month = int(month)
            day = int(day)
            year = int(year)

            if 1 <= month <= 12 and 1 <= day <= 31:
                break
        else:
            month, day, year = date.replace(",", "").split(" ")    

            month - month.index(months) + 1
            day = int(day)
            year = int(year)

            if 1 <= month <= 12 and 1 <= day <= 31:
                break
        print("Invalid date format.")    

    except (ValueError, IndexError):
        print("Invalid date format.")
        

print(f"{year:04}-{month:02}-{day:02}")    


