from pathlib import Path
import pandas as pd


def load_data():
    """
    Selects parent directory and loads data from CSV file.
    :return: Pandas df
    """
    base_dir = Path(__file__).resolve().parent.parent
    file_path = base_dir / "data" / "tripadvisor_hotel_reviews.csv"

    df = pd.read_csv(file_path)
    return df


if __name__ == "__main__":
    load_data()
