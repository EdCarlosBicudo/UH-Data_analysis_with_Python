
def reverse_dictionary(d):

    f = [item for sublist in d.values() for item in sublist]
    result = {}

    for i in f:
        result[i] = []
        for k, v in d.items():
            if i in v:
                result[i].append(k)

    return result

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    reverse_dictionary(d)
    print(d)

if __name__ == "__main__":
    main()
