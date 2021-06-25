import pandas as pd
import numpy as np


def read_series():
    inputs = []
    read = True
    while read:
        raw = input('Valores: ')
        if not raw:
            read = False
            break
        try:
            i,v = raw.split()
            inputs.append([i, v])
        except ValueError:
            print("ValueError")
            continue

    inputs = np.array(inputs)
    if len(inputs) == 0:
        return pd.Series()
    return pd.Series(inputs[:, 1], index=inputs[:, 0], dtype='object')

def main():
    read_series()


if __name__ == "__main__":
    main()
