import seaborn as sns
import matplotlib.pyplot as plt
import polars as pl
# from sklearn.preprocessing import LabelEncoder

# survived      Survival                0 = No, 1 = Yes
# pclass        Ticket class            1 = 1st, 2 = 2nd, 3 = 3rd
# sex           Sex
# age           Age in years
# sibsp         # of siblings / spouses aboard the Titanic
# parch         # of parents / children aboard the Titanic
# ticket        Ticket number
# fare          Passenger fare
# cabin         Cabin number
# embarked      Port of Embarkation     C = Cherbourg, Q = Queenstown, S = Southampton


def main():
    df = pl.scan_parquet("src/train.parquet")
    sns.set_theme(style="ticks", palette="pastel")

    titanic_passengers = df.select(
        pl.col("age").fill_null(pl.col("age").mean()),
        pl.col("survived").drop_nulls(),
        pl.col("pclass").fill_null(pl.col("pclass").mean()).alias("class"),
    )

    sns.boxplot(
        data=titanic_passengers.collect(),
        x="class",
        y="age",
        hue="survived",
        gap=0.2,
    )

    #   Plots -----------------------------------------------------------------
    plt.title("Passengers of the Titanic")
    plt.ylabel("Age")
    plt.xlabel("Ticket Class")

    # Saving the file to be used on the README
    plt.savefig("src/graphs/boxplot.png")


if __name__ == "__main__":
    main()
