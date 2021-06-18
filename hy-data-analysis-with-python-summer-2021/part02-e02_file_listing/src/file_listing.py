import re


def file_listing(filename="src/listing.txt"):
    result = []

    with open(filename, 'r') as f:
        for line in f:
            item = []
            item.append(int(re.search("[ ][0-9]{2,}[ ]", line)[0].strip()))
            item.append(re.search("[ ][a-z]{3,3}[ ]", line,re.IGNORECASE)[0].strip())
            item.append(int(re.search("[ ][0-9]{1,2}[ ][0-9]", line)[0].strip().split(' ')[0].strip()))
            item.append(int(re.search("[0-9]{2,}[:][0-9]{2,}", line)[0].strip().split(':')[0]))
            item.append(int(re.search("[0-9]{2,}[:][0-9]{2,}", line)[0].strip().split(':')[1]))
            item.append(re.search("[0-9]{2,}[:][0-9]{2,}[ ].*", line)[0].split(' ')[1].strip())

            result.append(tuple(item))

    return result

def main():
    print(file_listing())

if __name__ == "__main__":
    main()
