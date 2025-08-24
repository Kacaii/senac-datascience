def main():
    msg = """
    Usage:

        poetry run help                     Display this help message
        poetry run boxplot                  Display the Boxplot plot
        poetry run boxplot_no_outliers      Display the Boxplot plot with no outliers
        poetry run histogram                Display the Histogram plot
        poetry run kde                      Display the Kernel Density Estimation plot
    """

    print(msg)


if __name__ == "__main__":
    main()
