
def distinct_characters(L):
    result = {}

    for i in L:
        result[i] = len(set(i))

    return result

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
