import seaborn as sns
import matplotlib.pyplot as plt
import polars as pl

# survived      Survival                0 = No, 1 = Yes
# pclass        Ticket class            1 = 1st, 2 = 2nd, 3 = 3rd
# sex           Sex
# Age           Age in years
# sibsp         # of siblings / spouses aboard the Titanic
# parch         # of parents / children aboard the Titanic
# ticket        Ticket number
# fare          Passenger fare
# cabin         Cabin number
# embarked      Port of Embarkation     C = Cherbourg, Q = Queenstown, S = Southampton


def main():
    sns.set_theme(style="ticks", palette="pastel")
    df = pl.scan_parquet("src/train.parquet")

    sns.displot(df.collect(), x="age", kind="kde")
    plt.show()


if __name__ == "__main__":
    main()
