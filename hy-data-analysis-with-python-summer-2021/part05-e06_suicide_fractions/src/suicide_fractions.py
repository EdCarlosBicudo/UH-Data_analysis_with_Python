
import pandas as pd

def suicide_fractions():
    df = pd.read_csv("src/who_suicide_statistics.csv", index_col="country")

    df["mean_fraction"] = df["suicides_no"]/df["population"]
    df2 = df.groupby("country")[["mean_fraction"]].mean()
    return pd.Series(df2["mean_fraction"])

def main():
    print(suicide_fractions())

if __name__ == "__main__":
    main()
