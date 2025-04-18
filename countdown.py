def countdown(n):
    if n == 0:  # Base case (stopping condition)
        print("Blast off!")
        return  
    print(n)
    countdown(n - 1)  # Recursive call

countdown(5)
