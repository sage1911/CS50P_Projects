def main():
    counts = {}
    words = get_words("address.txt")
    lowercase_words = [words.lower() for word in words if len(word) > 4 ]

    for word in lowercase_words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word]  = 1

    save_counts(counts)           

main()