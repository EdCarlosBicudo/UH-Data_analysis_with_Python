
import re

def red_green_blue(filename="src/rgb.txt"):
    result = []
    with open(filename) as f:
        f.readline()
        for line in f.readlines():
            pattern = r"(\d+)\s+(\d+)\s+(\d+)\s+(.+)"

            match = re.match(pattern, line.strip())

            g = match.groups()
            result.append(f"{g[0]}\t{g[1]}\t{g[2]}\t{g[3]}")

    return result


def main():
    print(red_green_blue())

if __name__ == "__main__":
    main()
