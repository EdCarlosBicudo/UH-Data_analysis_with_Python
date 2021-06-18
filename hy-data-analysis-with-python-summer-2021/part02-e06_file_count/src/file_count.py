
import sys

def file_count(filename):

    with open(filename, 'r') as f:
        lines = 0
        words = 0
        characters = 0
        for line in f.readlines():
            lines += 1
            if line != '\n':
                words += len(line.split(' '))
            characters += len(line)

        return (lines, words, characters)

def main():
    for file in sys.argv[1:]:
        lines, words, characters = file_count(file)
        print(f"{lines}\t{words}\t{characters}\t{file}")

if __name__ == "__main__":
    main()
