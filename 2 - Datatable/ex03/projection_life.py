#!/usr/bin/env python3.10

from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Load life expectancy & income data from files and create a scatter plot.

    Returns:
        None
    """
    try:
        df1 = load("life_expectancy_years.csv")
        df2 = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        if df1 is None or df2 is None:
            raise FileNotFoundError()
        val1 = df1['1900']
        val2 = df2['1900']
        plt.scatter(val2, val1)
        plt.title("1900")
        plt.xlabel('Gross domestic product')
        plt.xscale('log')
        plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
        plt.ylabel('Life Expectancy')
        plt.yticks([20, 25, 30, 35, 40, 45, 50, 55])
        plt.show()
    except FileNotFoundError:
        print("Error: The CSV file was not found.")


if __name__ == "__main__":
    main()
