from pathlib import Path
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import json

# Finds the appropriate path for the file to be output to.
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)


def generate_wordcloud(tokens_series, title="Word Cloud"):
    """
    Generates a word cloud of the most common words used in reviews.
    :param tokens_series: A pandas series of strings containing words from the reviews.
    :param title: String
    :return: None
    """
    cleaned_tokens = []

    for item in tokens_series:

        # Case 1: already a list
        if isinstance(item, list):
            cleaned_tokens.extend(item)

        # Case 2: JSON string (from DB storage)
        elif isinstance(item, str) and item.startswith("["):
            cleaned_tokens.extend(json.loads(item))

        # Case 3: plain string (space-separated)
        elif isinstance(item, str):
            cleaned_tokens.extend(item.split())

    # Converts the pandas series into a long string of text.
    text = " ".join(cleaned_tokens)

    # Sets the dimensions fo the words cloud and the colour then generate it from the text.
    wc = WordCloud(width=800, height=400, background_color="white").generate(text)

    # Sets the figure dimensions and title.
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.title(title)

    # Save image
    file_path = OUTPUT_DIR / title
    plt.savefig(file_path)

    # Shows the image on screen.
    plt.show()
