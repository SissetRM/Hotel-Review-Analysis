from pathlib import Path
import pandas as pd

# Base output directory
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "outputs"

# Ensure folder exists
OUTPUT_DIR.mkdir(exist_ok=True)


def save_word_frequencies(word_list, filename="top_words.csv"):
    """
    Save word frequency list to CSV.
    :param word_list: list of tuples [(word, count), ...]
    :param filename: string
    :return: file_path
    """
    df = pd.DataFrame(word_list, columns=["word", "count"])
    file_path = OUTPUT_DIR / filename
    df.to_csv(file_path, index=False)
    return file_path


def save_cleaned_data(df, filename="cleaned_data.csv"):
    """
    Save cleaned dataframe for reuse.
    :param df: Pandas dataframe.
    :param filename: string
    :return: file_path
    """
    file_path = OUTPUT_DIR / filename
    df.to_csv(file_path, index=False)
    return file_path
