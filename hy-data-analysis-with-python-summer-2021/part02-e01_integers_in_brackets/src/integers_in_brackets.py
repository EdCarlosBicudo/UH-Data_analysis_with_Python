import re


def integers_in_brackets(s):
    aux = re.findall(r'\[\s*([-+]?\d+)\s*\]', s)
    return [int(x) for x in aux]


def main():
    print(integers_in_brackets("  afd [asd] [12 ] [a34]  [ -43 ]tt [+12]xxx"))

if __name__ == "__main__":
    main()
