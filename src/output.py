import sqlite3
from pathlib import Path
import pandas as pd
import json

# Base output directory
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "hotel_reviews.db"
print(DB_PATH)


def save_word_frequencies(word_list, table_name="top_words"):
    """
    Save word frequency list to CSV.
    :param word_list: list of tuples [(word, count), ...]
    :param table_name: string
    :return: file_path
    """
    df = pd.DataFrame(word_list, columns=["word", "count"])
    conn = sqlite3.connect(DB_PATH)
    if "tokens" in df.columns:
        df["tokens"] = df["tokens"].apply(json.dumps)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()

    return table_name


def save_cleaned_data(df, table_name="cleaned_data"):
    """
    Save cleaned dataframe for reuse.
    :param df: Pandas dataframe.
    :param table_name: string
    :return: table_name
    """
    conn = sqlite3.connect(DB_PATH)
    if "tokens" in df.columns:
        df["tokens"] = df["tokens"].apply(json.dumps)

    df.to_sql(table_name, conn, if_exists="replace", index=False)

    conn.close()

    return table_name
