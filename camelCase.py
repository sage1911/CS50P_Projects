def main():
    user_input = input("Name in camelCase: ")
    snake_case = ""

    for c in user_input:
        if c.isupper():
            snake_case += "_" + c.lower()
        else:
            snake_case += c    

    print(snake_case)                

main()