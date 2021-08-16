

import pandas as pd
from sklearn import linear_model


def coefficient_of_determination():
    df = pd.read_csv("src/mystery_data.tsv", sep="\t")
    X = df.iloc[:,0:5]
    y = df.iloc[:,5]
    model = linear_model.LinearRegression()
    model.fit(X, y)
    scores = []
    scores.append(model.score(X, y))
    for i in X:
        model.fit(df[i].values.reshape(-1, 1), y)
        score = model.score(df[i].values.reshape(-1, 1), y)
        scores.append(score)
    return scores

def main():
    scores = coefficient_of_determination()
    for i, n in enumerate(scores):
        if i==0:
            print(f"R2-score with feature(s) X: {n}")
        else:
            print(f"R2-score with feature(s) X{i+1}: {n}")


if __name__ == "__main__":
    main()
