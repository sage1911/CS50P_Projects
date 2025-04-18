import inflect


def main():
    p = inflect.engine()

    name_list = []

    try:

        while True:
            name = input("Enter a name: ").strip()
            name_list.append(name)

    except EOFError:
        pass

    farewell_message = f"Adieu, adieu, to {p.join(name_list)}"

    print(farewell_message)


if __name__ == "__main__":
    main()
