
def find_matching(L, pattern):
    result = []

    for count, value in enumerate(L):
        if pattern in value:
            result.append(count)

    return result

def main():
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))

if __name__ == "__main__":
    main()
