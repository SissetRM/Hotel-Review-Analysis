from src.data_loader import load_data
from src.cleaning import clean_text_column, tokenize_column
from src.analysis import get_top_words
from src.visualisation import generate_wordcloud


def main():
    df = load_data()
    print(df)
    df = clean_text_column(df, "Review")
    df = tokenize_column(df, "clean")

    top_words = get_top_words(df["tokens"])
    print(top_words[:10])

    generate_wordcloud(df["tokens"], title="Hotel Reviews")


if __name__ == "__main__":
    main()
