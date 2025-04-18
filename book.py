def main():
    with open("alice.txt", "r") as f:    
        contents = f.readlines()

    chapter1 = contents[89:313]
    with open("chapter1.txt", "w") as f:
        f.writelines(chapter1)


main()
