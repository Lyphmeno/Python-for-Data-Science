#!/usr/bin/env python3.10

import pandas as pd


def load(path: str) -> pd.dataFrame:
    """
    This function loads a CSV file into a pandas DataFrame.

    :param str: path of the file
    :returns:   Returns a pandas DataFrame containing the CSV.
                None if file not found
    :raises:    ValueError  
    """
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimension {df.shape}")
        return df
    except FileNotFoundError as e:
        print(f"{e}")
        return None
