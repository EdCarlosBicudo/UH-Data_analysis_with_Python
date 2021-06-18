
def word_frequencies(filename):
    result = {}

    with open(filename, 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                s = word.strip("""!"#$%&'()*,-./:;?@[]_""").strip('\n')
                if s == "creating":
                    print(f"{s} | creating")
                result[s] = result.get(s, 0) + 1

    return result

def main():
    print(word_frequencies('src/alice.txt'))

if __name__ == "__main__":
    main()
