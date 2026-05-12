from collections import Counter


def get_top_words(tokens_series, n=20):
    """
    Gets the 20 most common words.
    :param tokens_series: A Pandas series with the words used to describe the hotels.
    :param n: integer of the number of top words wanted.
    :return: A list of tuples. [(word, count), ...]
    """
    all_words = [word for tokens in tokens_series for word in tokens]

    # Counts the occurrences of every word and filters by the top 20 words.
    return Counter(all_words).most_common(n)


def get_top_words_by_group(df, group_col, token_col):
    """
    Finds the top words for each group (e.g. region).
    :param df: The pandas dataframe containing the data.
    :param group_col: Name of the column to group by (e.g. "region").
    :param token_col: Name of the column containing tokenised text (list of words per row).
    :return: Dictionary mapping each group to a list of (word, count) tuples.
         Example: {"London": [("hotel", 120), ("clean", 95), ...]}
    """
    result = {}
    for group in df[group_col].unique():
        tokens = df[df[group_col] == group][token_col]
        result[group] = get_top_words(tokens)
    return result
