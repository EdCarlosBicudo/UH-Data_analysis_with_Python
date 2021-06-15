
def sum_equation(L):
    if not L:
        return "0 = 0"

    s = " + ".join([str(n) for n in L])
    s += f" = {sum(L)}"
    return s

def main():
    print(sum_equation([1,5,7]))

if __name__ == "__main__":
    main()
