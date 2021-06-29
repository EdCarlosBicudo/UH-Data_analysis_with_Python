

import pandas as pd

def best_record_company():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    id = df.groupby('Publisher')['WoC'].sum().idxmax()
    return df[df['Publisher'] == id]

def main():
    df = best_record_company()
    print(df.head(2))


if __name__ == "__main__":
    main()
