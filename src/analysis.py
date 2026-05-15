from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report


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


def lr_rating(reviews, ratings):
    """
    Takes a dataframe of hotel reviews and their ratings and applies logistic regression to create
    a machine learning model able to predict the rating of a review.
    :param reviews:
    :param ratings:
    :return:
    """
    x = reviews  # text
    y = ratings  # target

    # Split the data into data used to create the model and data used to test the model.
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42
    )

    # Turn the raw text into numerical values of importance based on how often they appear.
    vectorizer = TfidfVectorizer(
        max_features=5000,
        ngram_range=(1, 2)  # Include two word phrases (e.g. "not good", "very clean").
    )
    x_train_vec = vectorizer.fit_transform(x_train)
    x_test_vec = vectorizer.transform(x_test)

    # A logistic Regression model is trained on the vectorised text data.
    model = LogisticRegression(max_iter=1000)
    model.fit(x_train_vec, y_train)

    # Predict the ratings of the test dataset.
    y_pred = model.predict(x_test_vec)

    # Create a report of the models accuracy when tested.
    print(classification_report(y_test, y_pred))

    # Output an example of a misclassified review.
    for i in range(len(y_test)):
        if y_test.iloc[i] != y_pred[i]:
            print("Review:", x_test.iloc[i])
            print("Actual:", y_test.iloc[i])
            print("Predicted:", y_pred[i])
            print("---")
            break
