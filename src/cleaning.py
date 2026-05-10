import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words("english"))


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    return text


def clean_text_column(df, column):
    df["clean"] = df[column].apply(clean_text)
    return df


def tokenize(text):
    tokens = word_tokenize(text)
    return [w for w in tokens if w not in stop_words and len(w) > 2]


def tokenize_column(df, column):
    df["tokens"] = df[column].apply(tokenize)
    return df
