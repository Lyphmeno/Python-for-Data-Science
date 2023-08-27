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
        val1 = df1.loc[1900]
        val2 = df2.loc[1900]
        plt.scatter(val1, val2)
        plt.ylabel('Life Expectancy')
        plt.xlabel('Gross domestic product')
        plt.title("1900")
        plt.show()
    except FileNotFoundError:
        print("Error: The CSV file was not found.")
    except Exception as e:
        print(f"{e}")


if __name__ == "__main__":
    main()
