

def extract_numbers(s):
    numbers = []

    for seq in s.split(' '):
        try:
            numbers.append(int(seq))
        except:
            try:
                numbers.append(float(seq))
            except:
                pass

    return numbers

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
