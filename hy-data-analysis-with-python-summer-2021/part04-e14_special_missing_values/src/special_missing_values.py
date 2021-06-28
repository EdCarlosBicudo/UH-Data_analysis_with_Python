
import pandas as pd
import numpy as np

def special_missing_values():
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')
    new_index = df.index[df['LW'] == "New"].tolist()
    re_index = df.index[df['LW'] == "Re"].tolist()
    df.iloc[new_index, 1] = np.nan
    df.iloc[re_index, 1] = np.nan

    df = df[df['Pos'].astype('float') > df['LW'].astype('float')]
    return df

def main():
    print(special_missing_values())

if __name__ == "__main__":
    main()
