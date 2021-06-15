import itertools

def detect_ranges(L):
    cL = L.copy()
    cL.sort()
    def aux(L):
        for i, j in itertools.groupby(enumerate(L), lambda x: x[1] - x[0]):
            j = list(j)
            start = j[0][1]
            length = len(j)

            if length == 1:
                yield start
            else:
                yield (start, start+length)
    return list(aux(cL))

def main():
    L = [4, 2, 0, -2, -4]
    print(L)
    result = detect_ranges(L)
    print(result)



if __name__ == "__main__":
    main()
