from pathlib import Path
import pandas as pd
import sqlite3


def load_csv_data():
    """
    Selects parent directory and loads data from CSV file.
    :return: df - A pandas dataframe.
    """
    base_dir = Path(__file__).resolve().parent.parent
    file_path = base_dir / "data" / "tripadvisor_hotel_reviews.csv"

    df = pd.read_csv(file_path)
    return df


# Base output directory
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "hotel_reviews.db"
CSV_PATH = BASE_DIR / "data" / "tripadvisor_hotel_reviews.csv"


def create_sql_database():
    """
    Loads CSV data into SQLite database.
    Run this once or when data changes.
    :return: None
    """
    conn = sqlite3.connect(DB_PATH)

    df = pd.read_csv(CSV_PATH)

    df.to_sql("reviews", conn, if_exists="replace", index=False)

    conn.close()


def load_sql_data_from_db():
    """
    Loads all review data from database.
    :return: df
    """
    conn = sqlite3.connect(DB_PATH)

    try:
        df = pd.read_sql("SELECT * FROM reviews", conn)
        conn.close()
        return df

    except (sqlite3.OperationalError, pd.errors.DatabaseError):
        print("No database or table found. Creating database...")
        conn.close()  # close before recreating

        create_sql_database()
        # Reconnect and load again
        conn = sqlite3.connect(DB_PATH)
        df = pd.read_sql("SELECT * FROM reviews", conn)
        conn.close()

        print("Database created and data loaded.")
        return df


if __name__ == "__main__":
    df_csv = load_csv_data()
    df_sql = load_sql_data_from_db()
