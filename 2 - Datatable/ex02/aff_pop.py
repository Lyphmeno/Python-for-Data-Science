#!/usr/bin/env python3.10

from load_csv import load
import matplotlib.pyplot as plt


def convert(value):
    """
    Convert short form number in float.

    Parameters:
        value: The short form number.

    Returns:
        float: The converted short form number.

    Raises:
        None
    """
    if (value[-1] == "M"):
        return float(value[:-1])
    else:
        return float(value)


def main():
    """
    Load life expectancy data for France from a CSV file and create a plot.

    Returns:
        None
    """
    try:
        df = load("population_total.csv")
        if df is None:
            raise FileNotFoundError()
        pop = df.set_index('country')
        val_be = pop.loc['Belgium'][:251].apply(convert)
        val_fr = pop.loc['France'][:251].apply(convert)
        years = val_be.index
        plt.plot(years, val_be, color='b', label='Belgium')
        plt.plot(years, val_fr, color='g', label='France')
        plt.xticks(years[::40])
        plt.yticks([20, 40, 60], ['20M', '40M', '60M'])
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.title('Population Projections')
        plt.legend(loc='lower right')
        plt.show()
    except FileNotFoundError:
        print("Error: The CSV file was not found.")
    except KeyError:
        print("Error: 'FRANCE' row or years column not found in the CSV file.")


if __name__ == "__main__":
    main()
