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

def get_credits(title, titles, credits, content_id=None):
    """
    Get the personnel credits associated with the content title.

    Parameters
    ----------
    title : string
        The content title from the `title` column of the content's row.
    titles : pandas.DataFrame
        The tabular data with content data.
    credits : pandas.DataFrame
        The tabular data with personnel credits.
    content_id : string, default=None
        Optional content ID from the `id` column of `titles`.

    Returns
    -------
    pandas.DataFrame
        The subset of the `credits` DataFrame representing the
         credits associated with `content_id`.

    Raises
    ------
    KeyError
        If `title` isn't unique in `titles` and `content_id`
         is None.
        If `title` doesn't exist in `titles`.
    """
    if content_id is None:
        content_id = titles[titles["title"] == title]["id"]
    if len(content_id) == 0:
        raise KeyError(
            f'"{title}" does not exist in `titles`.'
        )
    if len(content_id) != 1:
        raise KeyError(
            f'"{title}" is not a unique title. Please provide a `content_id`.'
        )
    content_id = content_id.values[0]
    return credits[credits["id"] == content_id]
