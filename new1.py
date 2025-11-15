
import zipfile
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    z = zipfile.ZipFile("../NLP/athlete_events.zip")
    df = pd.read_csv(z.open("athlete_events.csv"))
    df = df.dropna(subset=['Medal', "Age", "Height", "Weight"])

    # task1
    s1 = df[["ID", "Sex", "Medal"]].drop_duplicates()
    result1 = s1.groupby(by=["Medal", "Sex"]).count()
    print("Task 1:\n", result1, "\n")

    # task2
    result2 = df[df['Medal'] == 'Gold']["NOC"].value_counts()[:1]
    print("Task 2:\n", result2, "\n")

    # task3
    result3 = pd.crosstab(df['Sport'], df['Sex'], margins=True)
    print("Task 3:\n", result3, "\n")

    # task4
    slice4 = df[(df['Sex'] == 'F') & (df['Sport'] == 'Ice Hockey')]
    result4 = slice4['Age'].agg('std')
    print("Task 4:\n Standard deviation of Age for Females in Ice Hockey:", result4, "\n")

    # task5
    slice5 = df[(df['Medal'] == 'Bronze') & (df['Sex'] == 'F')][["ID", "NOC"]].drop_duplicates()
    result5 = slice5["NOC"].value_counts()[:4]
    print("Task 5:\n", result5, "\n")

    # task6
    countries = df["NOC"].value_counts()[:3].index
    slice6 = df[df["NOC"].isin(countries)][["NOC", "Medal"]]
    crosstab6 = pd.crosstab(slice6["NOC"], slice6["Medal"])
    print("Task 6:\n", crosstab6, "\n")
    crosstab6.plot(kind="bar")
    plt.title("Medals by top 3 countries")
    plt.show()

    # task7
    slice7 = df[(df['Sex'] == "M") & (df["Medal"] == "Silver")]["Weight"]
    print("Task 7: Density plot for Weight of Silver Medal Males")
    slice7.plot(kind='density')
    plt.title("Density of Weight (Silver Medal Males)")
    plt.xlabel("Weight")
    plt.show()

    # task8
    print("Task 8: Boxplot of Age by Medal type")
    sns.boxplot(y="Medal", x="Age", data=df)
    plt.title("Age distribution by Medal")
    plt.show()

    # task9
    slice9 = df[df['NOC'] == 'USA'][['Age', 'Weight', 'Height']]
    print("Task 9: Pairplot for USA athletes")
    sns.pairplot(slice9)
    plt.suptitle("Pairplot of Age, Weight, Height for USA athletes", y=1.02)
    plt.show()

if __name__ == "__main__":
    main()