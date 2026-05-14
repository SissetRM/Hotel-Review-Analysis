from src.cleaning import clean_text_column, tokenize_column
from src.analysis import get_top_words
from src.visualisation import generate_wordcloud
from src.output import save_word_frequencies, save_cleaned_data
from src.data_loader import load_sql_data_from_db


def main():
    """
    Main program which generates a word cloud from a CSV file of Tripadvisor reviews.
    :return: None
    """
    df = load_sql_data_from_db()

    df = clean_text_column(df, "Review")
    df = tokenize_column(df, "clean")
    print(df.head())

    # Analysis
    top_words = get_top_words(df["tokens"])
    print(top_words)

    # Save cleaned dataset
    save_cleaned_data(df)

    # Save results
    save_word_frequencies(top_words)

    generate_wordcloud(df["tokens"], title="Hotel Reviews")


if __name__ == "__main__":
    main()
