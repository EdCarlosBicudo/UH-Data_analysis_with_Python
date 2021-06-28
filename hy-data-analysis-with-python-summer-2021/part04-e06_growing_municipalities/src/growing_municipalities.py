
import pandas as pd

def growing_municipalities(df):
    positive_change =  df[df['Population change from the previous year, %'] > 0]
    proportion = (len(positive_change)/len(df))
    return round(proportion, 4)

def main():
    df = pd.read_csv('src/municipal.tsv', sep='\t')
    print(f"Proportion of growing municipalities: {growing_municipalities(df)*100:.1f}%")

if __name__ == "__main__":
    main()
