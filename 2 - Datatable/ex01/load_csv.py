#!/usr/bin/env python3.10

import pandas as pd


def load(path: str) -> pd.dataFrame:
    """
    Load a CSV file into a pandas DataFrame.

    Args:
        path (str): Path of the CSV file.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the loaded CSV data.
                      Returns None if the file is not found.

    Raises:
        FileNotFoundError: If the specified file is not found.
    """
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimension {df.shape}")
        return df
    except FileNotFoundError as e:
        print(f"{e}")
        return None
