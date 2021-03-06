

import pandas as pd


def cycling_weather():
    df1 = pd.read_csv("src/kumpula-weather-2017.csv")
    df2 = split_date()
    df = pd.merge(df1, df2, left_on=['Year', 'm','d'], right_on=['Year', 'Month', 'Day'])
    columns = ['m', 'd', 'Time', 'Time zone']
    df.drop(columns, axis=1, inplace=True)
    return df


def split_date():
	df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
	df2 = df["Päivämäärä"].str.split(expand=True)
	df2.dropna(inplace=True)
	df2.columns =  ["Weekday", "Day", "Month", "Year", "Hour"]
	df2["Hour"] = df2["Hour"].str.split(":", expand=True)[0]

	days = dict(zip("ma ti ke to pe la su".split(), "Mon Tue Wed Thu Fri Sat Sun".split()))
	months = dict(zip("tammi helmi maalis huhti touko kesä heinä elo syys loka marras joulu".split(), range(1,13)))

	df2["Weekday"] = df2["Weekday"].map(days)
	df2["Month"] = df2["Month"].map(months)
	df2 = df2.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})

	df.drop("Päivämäärä", axis=1, inplace=True)
	df.dropna(axis=0, how='all', inplace=True)
	df.dropna(axis=1, how='all', inplace=True)
	df = pd.concat([df2, df], axis=1)
	return df

def main():
    df = cycling_weather()
    print(df.head(2))

if __name__ == "__main__":
    main()
