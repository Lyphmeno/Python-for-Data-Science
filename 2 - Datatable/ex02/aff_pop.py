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
        years = [str(years) for years in range(1800, 2051)]
        val_fr = df.loc['FRANCE', years].tolist()
        val_be = df.loc['BELGIUM', years].tolist()
        plt.plot(years, val_fr, marker='o', label='FRANCE')
        plt.plot(years, val_be, marker='o', label='BELGIUM')
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.title('Population Projections')
        plt.legend()
        plt.show()
    except FileNotFoundError:
        print("Error: The CSV file was not found.")
    except KeyError:
        print("Error: 'FRANCE' row or years column not found in the CSV file.")
    except Exception as e:
        print(f"{e}")


if __name__ == "__main__":
    main()
