
def merge(L1, L2):
    cL1 = L1.copy()
    cL2 = L2.copy()

    lenght = len(cL1) + len(cL2)

    final = []
    for _ in range(lenght):
        n = None

        if len(cL1) > 0:
            if len(cL2) > 0:
                if cL1[0] < cL2[0]:
                    n = cL1.pop(0)
                else:
                    n = cL2.pop(0)
            else:
                n = cL1.pop(0)
        else:
            n = cL2.pop(0)

        final.append(n)

    return final

def main():
    l1 = [1, 5, 9, 12]
    l2= [2, 6, 10]
    print(merge(l1, l2))

if __name__ == "__main__":
    main()
