"""Module for reading in raw data from CSV files."""

import os
import pandas as pd

def load(directory):
    """
    Load Netflix titles and credits from directory.

    Parameters
    ----------
    directory : pathlike
        Path to directory containing CSV files "titles.csv" and
         "credits.csv"
    
    Returns
    -------
    pandas.DataFrame
        Netflix movie and show titles.
    pandas.DataFrame
        Personnel credits for Netflix content.
    """
    assert os.path.exists(directory), (
        f"Couldn't find `{directory}`"
    )
    titles_path = os.path.join(directory, "titles.csv")
    credits_path = os.path.join(directory, "credits.csv")
    assert os.path.exists(titles_path) and os.path.exists(credits_path), (
        '"titles.csv" and "credits.csv" must exist in `directory`.'
    )
    titles = pd.read_csv(titles_path)
    credits = pd.read_csv(credits_path)
    return titles, credits
