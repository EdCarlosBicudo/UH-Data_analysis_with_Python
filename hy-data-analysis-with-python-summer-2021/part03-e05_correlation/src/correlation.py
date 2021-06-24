import scipy.stats
import numpy as np

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    data = load()
    corr, _ = scipy.stats.pearsonr(data[:, 0], data[:, 2])
    return corr

def correlations():
    data = load()

    ls = data[:, 0]
    sw = data[:, 1]
    pl = data[:, 2]
    pw = data[:, 3]

    return np.corrcoef([ls, sw, pl, pw])

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
