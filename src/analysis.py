from collections import Counter


def get_top_words(tokens_series, n=20):
    all_words = [word for tokens in tokens_series for word in tokens]
    return Counter(all_words).most_common(n)


def get_top_words_by_group(df, group_col, token_col):
    result = {}
    for group in df[group_col].unique():
        tokens = df[df[group_col] == group][token_col]
        result[group] = get_top_words(tokens)
    return result
