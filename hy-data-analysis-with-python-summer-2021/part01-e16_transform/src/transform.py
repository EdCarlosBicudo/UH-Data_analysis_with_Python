
def transform(s1, s2):
    if not s1 and not s2:
        return []
    l1 = list(map(lambda x: int(x), s1.split(' ')))
    l2 = list(map(lambda x: int(x), s2.split(' ')))

    result = []
    for i1, i2 in zip(l1, l2):
        result.append(i1*i2)

    return result

def main():
    s1 = "1 5 3"
    s2 = "2 6 -1"
    result = transform("", "")
    print(result)

if __name__ == "__main__":
    main()
