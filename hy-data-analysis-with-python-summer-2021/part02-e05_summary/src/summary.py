
import sys
import numpy as np
import statistics

def summary(filename):
    numbers = []

    with open(filename, 'r') as f:
        for line in f.readlines():
            try:
                n = float(line)
                numbers.append(n)
            except ValueError:
                pass

    sum = np.sum(numbers)
    average = np.average(numbers)
    std = statistics.stdev(numbers)

    return (sum,average,std)

def main():
    for file in sys.argv[1:]:
        sum, ave, std = summary(file)
        print(f"File: {file} Sum: {sum:.6f} Average: {ave:.6f} Stddev: {std:.6f}")

if __name__ == "__main__":
    main()
