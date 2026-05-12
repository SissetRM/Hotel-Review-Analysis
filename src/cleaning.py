import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# A list of words like "A", "you",  and "because" we are not interested in.
stop_words = set(stopwords.words("english"))


def clean_text(text):
    """
    Transforms a string text to lowercase and removes plurals.
    :param text: String
    :return: text
    """
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    return text


def clean_text_column(df, column):
    """
    Transforms a pandas column of text to lowercase and removes the plurals
    :param df: A pandas dataframe
    :param column: A pandas column
    :return: df
    """
    df["clean"] = df[column].apply(clean_text)
    return df


def tokenize(text):
    """
    Splits sentences into strings of text with a length greater than 2 with no stop words.
    :param text: A string containing a sentence.
    :return: A list of strings.
    """
    tokens = word_tokenize(text)
    return [w for w in tokens if w not in stop_words and len(w) > 2]


def tokenize_column(df, column):
    """
    Converts a column of sentences in a pandas dataframe to a column of a list of strings.
    :param df: A pandas dataframe.
    :param column: A pandas column.
    :return: df
    """
    df["tokens"] = df[column].apply(tokenize)
    return df
