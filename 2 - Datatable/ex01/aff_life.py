#!/usr/bin/env python3.10

from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Load life expectancy data for France from a CSV file and create a plot.

    Returns:
        None
    """
    try:
        df = load("life_expectancy_years.csv")
        if df is None:
            raise FileNotFoundError()
        years = df.columns.tolist()[1:]
        val = df.loc['FRANCE', years].tolist()
        plt.plot(years, val, marker='o', label='FRANCE')
        plt.xlabel('Year')
        plt.ylabel('Life Expectancy')
        plt.title('France Life expectancy Projections')
        plt.legend()
        plt.show()
    except FileNotFoundError:
        print("Error: The CSV file was not found.")
    except KeyError:
        print("Error: 'FRANCE' row or years column not found in the CSV file.")

if __name__ == "__main__":
    main()
