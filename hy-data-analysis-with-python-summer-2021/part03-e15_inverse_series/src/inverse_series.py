
import pandas as pd

def inverse_series(s):
    index = s.index
    values = s.values
    return pd.Series(index, index=values)

def main():
    s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
    print(inverse_series(s1))

if __name__ == "__main__":
    main()
